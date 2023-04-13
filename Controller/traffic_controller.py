import time
import Controller.Light as light
import Controller.encoder as encoder
import Controller.ConnectedClient as connected_client
import Controller.socket_server as server
import Controller.TrafficLights as traffic_lights
import Controller.vehicle_priorities as vehicle_priorities

motorized_vehicle_time = 7
orange_wait_time = 3
clear_traffic_time = 3

# id of all traffic lights
bus_id = float(42.0)
train_id = float(99.0)

lights_id_array = [bus_id,
                   train_id,
                   float(1.1),
                   float(2.1),
                   float(5.1),
                   float(6.1),
                   float(7.1),
                   float(8.1),
                   float(9.1),
                   float(10.1),
                   float(11.1),
                   float(12.1),
                   float(35.1), float(35.2), float(36.1), float(36.2),  # pedestrian_west
                   float(37.2), float(37.1), float(38.1), float(38.2),  # pedestrian_north
                   float(31.2), float(31.1), float(32.1), float(32.2),  # pedestrian_east
                   float(86.1), float(26.1),  # bike_lane_west
                   float(88.1), float(28.1),  # bike_lane_north
                   float(22.0)  # bike_lane_east
                   # float(152.0), float(154.0), float(160.0)
                   ]

green_stages = [
    [float(1.1), float(2.1), float(7.1), float(8.1), 0],

    [float(5.1), float(10.1), float(11.1), 0],

    [float(6.1), float(12.1), 0],

    # [float(9.1), 0],

    [float(35.1), float(35.2), float(36.1), float(36.2),  # pedestrian_west
     float(86.1), float(26.1),  # bike_lane_west
     float(5.1), float(11.1), 0],

    [float(37.2), float(37.1), float(38.1), float(38.2),
     float(88.1), float(28.1),
     float(2.1), float(7.1), float(8.1), 0],

    [float(31.2), float(31.1), float(32.1), float(32.2),
     float(22.0),
     float(7.1), float(9.1), 0]
]

priority_green_stages = [
    [float(42.0), float(7.1), float(8.1), "bus_green_stage"],
    [float(99.0), float(1.1), float(2.1), float(8.1), "train_green_stage"],
    [float(99.0), float(42.0), float(8.1), "train_and_bus_green_stage"]
]

traffic_lights_array = traffic_lights.ReturnTrafficLights()
connected_client_array = connected_client.ReturnConnectedClient()


# initialize light objects
def init_lights():
    lights_array = []

    for i in range(0, len(lights_id_array)):
        lights_array.append(light.Light(lights_id_array[i], status=0, weight=0, red_time=0))

    traffic_lights_array.traffic_lights = lights_array


def handle_connection():
    current_connection = connected_client_array.connected_client

    # set first green stage and start timer
    current_green_stage = get_green_stage(get_deserialized_JSON(current_connection))
    set_lights_green(current_green_stage)
    server.send(encoder.serialize(traffic_lights_array.traffic_lights))
    start_time = time.time()

    while True:
        # wait for green stage to end
        if time.time() - start_time >= motorized_vehicle_time:
            status_sequence(current_connection, current_green_stage)

            # set next green stage and reset timer
            current_green_stage = get_green_stage(get_deserialized_JSON(current_connection))
            set_lights_green(current_green_stage)
            server.send(encoder.serialize(traffic_lights_array.traffic_lights))

            start_time = time.time()
        else:
            continue


def status_sequence(current_connection, current_green_stage):
    # receive JSON, set green lights to orange and wait for orange time
    get_deserialized_JSON(current_connection)
    set_lights_orange(current_green_stage)
    server.send(encoder.serialize(traffic_lights_array.traffic_lights))
    time.sleep(orange_wait_time)

    # receive JSON, set orange lights to red and wait for traffic clear time
    get_deserialized_JSON(current_connection)
    set_lights_red()
    server.send(encoder.serialize(traffic_lights_array.traffic_lights))
    time.sleep(clear_traffic_time)

def get_deserialized_JSON(current_connection):
    received_JSON = server.receive(connection=current_connection[0], client_address=current_connection[1])
    deserialized_JSON = encoder.deserialize(received_JSON)

    return deserialized_JSON


def get_green_stage(deserialized_JSON):
    # set the weights for the Light objects
    weighted_lights_array = set_weight(deserialized_JSON)

    # if there are priority vehicles, get the green stage with the most priority
    if check_vehicle_priorities() != False:
        green_stage = check_vehicle_priorities()

    # if there are no priority vehicles calculate the green stage with the most weight
    else:
        calculated_weights_array = calculate_green_stage_weights(weighted_lights_array)
        green_stage = sort_green_stage_weights(calculated_weights_array)

    print("GREEN STAGE IS:", green_stage)
    return green_stage


def set_weight(deserialized_JSON):
    weighted_lights_array = traffic_lights_array.traffic_lights

    for i in range(len(weighted_lights_array)):

        for j in range(len(deserialized_JSON)):

            if weighted_lights_array[i].id == deserialized_JSON[j][0]:
                weighted_lights_array[i].weight = deserialized_JSON[j][1]

    traffic_lights_array.traffic_lights = weighted_lights_array

    # for k in range(len(weighted_lights_array)):
    #     print(weighted_lights_array[k].id, weighted_lights_array[k].status, weighted_lights_array[k].weight)

    return weighted_lights_array


def check_vehicle_priorities():
    # train prio
    if vehicle_priorities.check(train_id):
        if vehicle_priorities.check(bus_id):
            return [tb for tb in priority_green_stages if tb[-1] == "train_and_bus_green_stage"][0]
        return [t for t in priority_green_stages if t[-1] == "train_green_stage"][0]

    elif vehicle_priorities.check(bus_id):
        return [b for b in priority_green_stages if b[-1] == "bus_green_stage"][0]

    else:
        return False


def calculate_green_stage_weights(weighted_lights_array):
    for i in range(len(green_stages)):
        green_stage_total_weight = 0
        for j in range(len(green_stages[i])):
            for k in range(len(weighted_lights_array)):
                if green_stages[i][j] == weighted_lights_array[k].id:
                    green_stage_total_weight += weighted_lights_array[k].weight

        green_stages[i][-1] = green_stage_total_weight

    return green_stages


def sort_green_stage_weights(calculated_weights_array):
    sorted_green_stages = sorted(calculated_weights_array, key=lambda x: x[-1], reverse=True)

    return sorted_green_stages[0]


def set_lights_red():
    set_lights_array = traffic_lights_array.traffic_lights

    for i in range(len(set_lights_array)):
        set_lights_array[i].status = 0

    traffic_lights_array.traffic_lights = set_lights_array


def set_lights_orange(green_stage):
    set_lights_array = traffic_lights_array.traffic_lights

    for j in range(len(green_stage)):
        for k in range(len(set_lights_array)):
            if green_stage[j] == set_lights_array[k].id:
                set_lights_array[k].status = 1

    traffic_lights_array.traffic_lights = set_lights_array


def set_lights_green(green_stage):
    set_lights_array = traffic_lights_array.traffic_lights

    for j in range(len(green_stage)):
        for k in range(len(set_lights_array)):
            if green_stage[j] == set_lights_array[k].id:
                set_lights_array[k].status = 2

    traffic_lights_array.traffic_lights = set_lights_array

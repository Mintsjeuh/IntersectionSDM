import Controller.Light as light
import Controller.encoder as encoder
import Controller.ConnectedClient as connected_client
import Controller.socket_server as server
import Controller.TrafficLights as traffic_lights
import Controller.vehicle_priorities as vehicle_priorities
import Controller.Timer as Timer

motorized_vehicle_time = 7
orange_wait_time = 3
traffic_clear_time = 3

train_cross_time = 10
train_barriers_time = 3
train_clear_time = 3

bus_id = float(42.0)
train_ids = [float(160.0), float(154.0), float(152.0)]
bike_lane_ids = [float(86.1), float(26.1), float(88.1), float(28.1), float(22.0)]

barriers_id = float(99.0)

lights_id_array = [bus_id,
                   barriers_id,
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
                   float(22.0),  # bike_lane_east
                   train_ids[0], train_ids[1], train_ids[2]
                   ]

green_stages = [
    [float(1.1), float(2.1), float(7.1), float(8.1), 0],

    [float(5.1), float(10.1), float(11.1), 0],

    [float(1.1), float(7.1), float(12.1), 0],

    [float(35.1), float(35.2), float(36.1), float(36.2),  # pedestrian_west
     float(86.1), float(26.1),  # bike_lane_west
     float(5.1), float(11.1), 0],


    [float(6.1),
     float(37.2), float(37.1), float(38.1), float(38.2),  # pedestrian_north
     float(88.1), float(28.1), 0],

    [float(31.2), float(31.1), float(32.1), float(32.2),  # pedestrian_east
     float(22.0),
     float(7.1), float(9.1), 0]
]

priority_green_stages = [
    [float(42.0), float(7.1), float(8.1), "bus_green_stage"],
    [float(160.0), float(1.1), float(2.1), float(8.1), "train_green_stage"],
    [float(160.0), float(42.0), float(8.1), "train_and_bus_green_stage"]
]

traffic_lights_array = traffic_lights.ReturnTrafficLights()
connected_client_array = connected_client.ReturnConnectedClient()
traffic_timer = Timer.Timer()

# initialize light objects
def init_lights():
    lights_array = []

    for i in range(0, len(lights_id_array)):
        lights_array.append(light.Light(lights_id_array[i], status=0, weight=0, red_time=0))

    traffic_lights_array.traffic_lights = lights_array


def handle_connection():
    current_connection = connected_client_array.connected_client
    tick = 0

    motorized_vehicle_green_stage = False
    bus_green_stage = False
    train_green_stage = False

    deserialized_JSON = get_deserialized_JSON(current_connection)
    current_green_stage = get_green_stage(deserialized_JSON)

    if tick == 0:
        if str(current_green_stage[-1]).__contains__("train"):
            motorized_vehicle_green_stage = False
            train_green_stage = True
            if str(current_green_stage[-1].__contains__("bus")):
                bus_green_stage = True

        elif str(current_green_stage[-1].__contains__("bus")):
            motorized_vehicle_green_stage = False
            bus_green_stage = True
            train_green_stage = False
        else:
            motorized_vehicle_green_stage = True
            bus_green_stage = False
            train_green_stage = False


    set_lights_green(current_green_stage, motorized_vehicle_green_stage, train_green_stage)
    server.send(encoder.serialize(traffic_lights_array.traffic_lights, traffic_timer))

    while True:
        print("Timer: ", traffic_timer.remainingTime)
        deserialized_JSON = get_deserialized_JSON(current_connection)
        if deserialized_JSON is not None:
            if tick == 0:
                if str(current_green_stage[-1]).__contains__("train"):
                    motorized_vehicle_green_stage = False
                    train_green_stage = True
                    if str(current_green_stage[-1].__contains__("bus")):
                        bus_green_stage = True

                elif str(current_green_stage[-1].__contains__("bus")):
                    motorized_vehicle_green_stage = False
                    bus_green_stage = True
                    train_green_stage = False
                else:
                    motorized_vehicle_green_stage = True
                    bus_green_stage = False
                    train_green_stage = False

            tick += 1
            print(tick)

            # handle train ticks
            if train_green_stage is True:
                if tick / 2 == train_cross_time:
                    # receive JSON, set green lights to orange and wait for orange time
                    set_lights_orange(current_green_stage, motorized_vehicle_green_stage, train_green_stage)

                if tick / 2 == train_cross_time + train_barriers_time:
                    # receive JSON, set orange lights to red and wait for traffic clear time
                    set_lights_red()

                if tick / 2 == train_cross_time + train_barriers_time + train_clear_time:
                    tick = 0
                    current_green_stage = get_green_stage(deserialized_JSON)
                    set_lights_green(current_green_stage, motorized_vehicle_green_stage, train_green_stage)

            # handle motorized vehicle tick
            if motorized_vehicle_green_stage is True:
                if tick / 2 == motorized_vehicle_time:
                    # receive JSON, set green lights to orange and wait for orange time
                    set_lights_orange(current_green_stage, motorized_vehicle_green_stage, train_green_stage)

                if tick / 2 == motorized_vehicle_time + orange_wait_time:
                    # receive JSON, set orange lights to red and wait for traffic clear time
                    set_lights_red()

                if tick / 2 == motorized_vehicle_time + orange_wait_time + traffic_clear_time:
                    tick = 0
                    current_green_stage = get_green_stage(deserialized_JSON)
                    set_lights_green(current_green_stage, motorized_vehicle_green_stage, train_green_stage)

            server.send(encoder.serialize(traffic_lights_array.traffic_lights, traffic_timer))


def get_deserialized_JSON(current_connection):
    received_JSON = server.receive(connection=current_connection[0], client_address=current_connection[1])
    deserialized_JSON = encoder.deserialize(received_JSON)

    return deserialized_JSON


def get_green_stage(deserialized_JSON):
    # set the weights for the Light objects
    weighted_lights_array = set_weight(deserialized_JSON)

    # if there are priority vehicles, get the green stage with the most priority
    if check_vehicle_priorities() is not False:
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

    for i in range(len(train_ids)):
        if vehicle_priorities.check(train_ids[i]):
            if vehicle_priorities.check(bus_id):
                green_stage = [tb for tb in priority_green_stages if tb[-1] == "train_and_bus_green_stage"][0]
            else:
                green_stage = [t for t in priority_green_stages if t[-1] == "train_green_stage"][0]
            green_stage[0] = train_ids[i]
            return green_stage

    if vehicle_priorities.check(bus_id):
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
        if set_lights_array[i].id == barriers_id:
            set_lights_array[i].status = 2
        else:
            set_lights_array[i].status = 0

    traffic_lights_array.traffic_lights = set_lights_array


def set_lights_orange(green_stage, motorized_vehicle_green_stage, train_green_stage):
    set_lights_array = traffic_lights_array.traffic_lights

    for j in range(len(green_stage)):
        for k in range(len(set_lights_array)):

            if set_lights_array[k].id == barriers_id:
                if motorized_vehicle_green_stage is True:
                    set_lights_array[k].status = 2
                elif train_green_stage is True:
                    set_lights_array[k].status = 1

            elif green_stage[j] == set_lights_array[k].id:
                set_lights_array[k].status = 1

    traffic_lights_array.traffic_lights = set_lights_array


def set_lights_green(green_stage, motorized_vehicle_green_stage, train_green_stage):
    set_lights_array = traffic_lights_array.traffic_lights

    for j in range(len(green_stage)):
        for k in range(len(set_lights_array)):

            if set_lights_array[k].id == barriers_id:
                if motorized_vehicle_green_stage is True:
                    set_lights_array[k].status = 2
                elif train_green_stage is True:
                    set_lights_array[k].status = 0

            elif green_stage[j] == set_lights_array[k].id:
                set_lights_array[k].status = 2

    traffic_lights_array.traffic_lights = set_lights_array




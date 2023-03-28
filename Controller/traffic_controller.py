import Controller.Light as light
import Controller.encoder as encoder
import Controller.ConnectedClient as connected_client
import Controller.socket_server as server
import Controller.TrafficLights as traffic_lights

# id of all traffic lights
lights_id_array = [float(42.0), float(1.1), float(2.1), float(5.1), float(6.1), float(7.1), float(8.1), float(9.1), float(10.1), float(11.1), float(12.1)]

green_stages = [
    [float(1.1), float(2.1), float(7.1), float(8.1)],
    [float(5.1), float(7.1), float(10.1), float(11.1)],
    [float(6.1), float(12.1)],
    [float(9.1)],
    [float(42.0), float(8.1), float(7.1)]
]

traffic_lights_array = traffic_lights.ReturnTrafficLights()
connected_client_array = connected_client.ReturnConnectedClient()

# initialize light objects
def initialize_lights():
    lights_array = []

    for i in range(0, len(lights_id_array)):
        lights_array.append(light.Light(lights_id_array[i], status=0, weight=0))
    traffic_lights_array.traffic_lights = lights_array


def handle_connection():
    current_connection = connected_client_array.connected_client
    while (True):
        received_JSON = server.receive(connection=current_connection[0], client_address=current_connection[1])
        deserialized_JSON = encoder.deserialize(received_JSON)

        weighted_lights_array = set_weight(deserialized_JSON)
        calculated_weights_array = calculate_green_stage_weights(weighted_lights_array)
        green_stage = sort_green_stages(calculated_weights_array)
        set_lights_array = set_lights(green_stage)
        # for i in range(len(set_lights_array)):
        #     print(weighted_lights_array[i].id, weighted_lights_array[i].status, weighted_lights_array[i].weight)
        print(traffic_lights_array.traffic_lights)
        server.send(encoder.serialize(traffic_lights_array.traffic_lights))




def set_weight(deserialized_JSON):
    weighted_lights_array = traffic_lights_array.traffic_lights
    for i in range (len(weighted_lights_array)):
        if (weighted_lights_array[i].id == deserialized_JSON[i][0]):
            weighted_lights_array[i].weight = deserialized_JSON[i][1]

    traffic_lights_array.traffic_lights = weighted_lights_array

    # for j in range(len(weighted_lights_array)):
    #     print(weighted_lights_array[j].id, weighted_lights_array[j].status, weighted_lights_array[j].weight)

    return weighted_lights_array


def calculate_green_stage_weights(weighted_lights_array):
    for i in range(len(green_stages)):
        green_stage_total_weight = 0
        for j in range(len(green_stages[i])):
            for k in range(len(weighted_lights_array)):
                if green_stages[i][j] == weighted_lights_array[k].id:
                    green_stage_total_weight += weighted_lights_array[k].weight

        green_stages[i].append(green_stage_total_weight)
    return green_stages


def sort_green_stages(calculated_weights_array):
    sorted_green_stages = sorted(calculated_weights_array, key=lambda x: x[-1], reverse=True)
    for i in range(len(sorted_green_stages)):
        sorted_green_stages[i].pop()

    return sorted_green_stages[0]


def set_lights(green_stage):
    set_lights_array = traffic_lights_array.traffic_lights

    for i in range(len(set_lights_array)):
        set_lights_array[i].status = 0

    for j in range(len(green_stage)):
        for k in range(len(set_lights_array)):
            if green_stage[j] == set_lights_array[k].id:
                set_lights_array[k].status = 2

    traffic_lights_array.traffic_lights = set_lights_array

    return set_lights_array

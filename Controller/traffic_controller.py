import Controller.Light as light
import Controller.encoder as encoder
import Controller.ConnectedClient as connected_client
import Controller.socket_server as server
import Controller.TrafficLights as traffic_lights

# id of all traffic lights
lights_id_array = [float(2.1),
                   float(5.1),
                   float(8.1),
                   float(11.1)]

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

    received_JSON = server.receive(connection=current_connection[0], client_address=current_connection[1])
    deserialized_JSON = encoder.deserialize(received_JSON)

    weighted_lights_array = set_weight(deserialized_JSON)
    print("WEIGHTED:", weighted_lights_array[0].id)

    # sorted_lights_array = set_priority(weighted_lights_array)

    # traffic_lights_array = traffic_lights.ReturnTrafficLights.traffic_lights




def set_weight(received_string):
    weighted_lights_array = []
    # set weights of all traffic lights with received string
    lights_array = traffic_lights_array.traffic_lights

    # lights_array = weighted_lights_array
    return lights_array

    # for i in range(len(received_string)):
    #     if ():
    #         id = deserialized_JSON[i][0]
    #         weight = deserialized_JSON[i][1]


def set_priority(lights_array):
    sorted_lights_array = []
    for i in range(0, len(lights_array)):
        if (lights_array[i].id == "8.1"):
            lights_array[i].weight = 5


def calculate_priority(lights_array):
    lights_array_sorted = sorted(lights_array, key=lambda x: x.weight, reverse=True)

    # print weight values
    for i in range(0, len(lights_array_sorted)):
        print(lights_array_sorted[i].weight)

    lights_array = set_lights(lights_array_sorted)
    return lights_array


def set_lights(lights_array):
    lights_array[0].status = 2
    return lights_array

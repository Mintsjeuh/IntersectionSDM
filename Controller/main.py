import Controller.Light as light
import Controller.encoder as encoder
import Controller.traffic_controller as controller
import Controller.socket_server as server

#id of all traffic lights
lights_id_array = [float(2.1),
                   float(5.1),
                   float(8.1),
                   float(11.1)]

#array to store traffic light objects
lights_array = []

#example of JSON send to the controller by the simulator
received_JSON = '[{"id": 2.1, "weight": 20},' \
                ' {"id": 5.1, "weight": 10},' \
                ' {"id": 8.1, "weight": 3},' \
                ' {"id": 11.1, "weight": 15}]'

def main():

    init_lights()
    print("Lights objects array: ", lights_array)

    lights_array_JSON = encoder.serialize(lights_array)
    print("JSONified string: ", lights_array_JSON)
    server.initialize()

    server.send(lights_array_JSON)
    deserialized_JSON = encoder.deserialize(server.receive())

    print("Deserialized JSON: ", deserialized_JSON)

    controller.set_weight(deserialized_JSON, lights_array)
    #send JSON to simulator
    #receive JSON from simulator

    #Set lights_array with values from deserialized_JSON
    #Match id and set weight to correct object

    #lights_array_weighted = controller.set_priority(lights_array)
    #lights_array_sorted = controller.calculate_priority(lights_array_weighted)
    #print(lights_array_sorted[0].id, lights_array_sorted[0].status, lights_array_sorted[0].weight)
    #traffic_controller to set lights

#initialize light objects
def init_lights():
    for i in range(0, len(lights_id_array)):
        lights_array.append(light.Light(lights_id_array[i], status=0, weight=0))

#run main method
if __name__ == "__main__":
    main()

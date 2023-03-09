import Controller.Light as light
import Controller.encoder as encoder
import Controller.traffic_controller as controller

lights_id_array = ["2.1", "5.1", "8.1", "11.1"]
lights_array = []

def main():
    init_lights()
    lights_array_JSON = encoder.serialize(lights_array)
    #send JSON to simulator
    #receive JSON from simulator
    lights_array_weighted = controller.set_priority(encoder.deserialize(lights_array_JSON))
    lights_array_sorted = controller.calculate_priority(lights_array_weighted)
    print(lights_array_sorted[0].id, lights_array_sorted[0].status, lights_array_sorted[0].weight)
    #traffic_controller to set lights

def init_lights():
    for i in range(0, len(lights_id_array)):
        lights_array.append(light.Light(lights_id_array[i], status=0, weight=0))

if __name__ == "__main__":
    main()
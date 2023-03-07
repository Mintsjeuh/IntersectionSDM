import Controller.Light as light
import Controller.encoder as encoder

lights_id_array = ["2.1", "5.1", "8.1", "11.1"]
lights_array = []

def main():
    init_lights()
    lights_array_JSON = encoder.serialize(lights_array)
    encoder.deserialize(lights_array_JSON)

def init_lights():
    for i in range(0, len(lights_id_array)):
        lights_array.append(light.Light(lights_id_array[i], 0))

if __name__ == "__main__":
    main()
import Controller.Light as light

def set_weight(deserialized_JSON, lights_array):
    for i in range(len(deserialized_JSON)):
        if ():
            id = deserialized_JSON[i][0]
            weight = deserialized_JSON[i][1]
    return lights_array

def set_priority(lights_array):
    for i in range(0, len(lights_array)):
        if (lights_array[i].id == "8.1"):
            lights_array[i].weight = 5
    return lights_array

def calculate_priority(lights_array):
    lights_array_sorted = sorted(lights_array, key=lambda x: x.weight, reverse=True)

    #print weight values
    for i in range(0, len(lights_array_sorted)):
        print(lights_array_sorted[i].weight)

    lights_array = set_lights(lights_array_sorted)
    return lights_array

def set_lights(lights_array):
    lights_array[0].status = 2
    return lights_array
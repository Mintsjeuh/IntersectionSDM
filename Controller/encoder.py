import json
from types import SimpleNamespace
import Controller.Light as light


lights_array_JSON = []
lights_array = []

def serialize(lights_array):
    for i in range(0, len(lights_array)):
        if(isinstance(lights_array[i], light.Light)):
            lights_array_JSON.append({'id' : lights_array[i].id, 'status' : lights_array[i].status})

    return json.dumps(lights_array_JSON, default=serialize)

    raise TypeError(f'Object {lights_array[i]} is not of type Lights')


def deserialize(lights_array_JSON):
    lights_array_JSON = json.loads(lights_array_JSON)
    for i in range (0, len(lights_array_JSON)):
        lights_array.append(light.Light(lights_array_JSON[i]['id'], lights_array_JSON[i]['status']))
        print(lights_array[i].id, lights_array[i].status)
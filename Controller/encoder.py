import json
import Controller.Light as light


def serialize(lights_array):
    lights_array_JSON = []
    for i in range(0, len(lights_array)):
        if isinstance(lights_array[i], light.Light):
            lights_array_JSON.append({'id': lights_array[i].id, 'status': lights_array[i].status})
        else:
            raise TypeError(f'Object {lights_array[i]} is not of type Lights')

    return json.dumps(lights_array_JSON, default=serialize)


def deserialize(lights_array_JSON):
    deserialized_JSON = []
    lights_array_JSON = json.loads(lights_array_JSON)
    for i in range (0, len(lights_array_JSON)):
        deserialized_JSON.append([lights_array_JSON[i]['id'], lights_array_JSON[i]['weight']])

    return deserialized_JSON

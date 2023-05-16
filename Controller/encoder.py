import json
import Controller.Light as light

def serialize(lights_array, traffic_timer):
    lights_array_JSON = []
    traffic_timer_JSON = {"id": traffic_timer.id, "status": traffic_timer.status, "remainingTime": traffic_timer.remainingTime}

    for i in range(0, len(lights_array)):
        if isinstance(lights_array[i], light.Light):
            lights_array_JSON.append({'id': lights_array[i].id, 'status': lights_array[i].status})
        else:
            raise TypeError(f'Object {lights_array[i]} is not of type Lights')

    array_JSON = {"trafficlights": lights_array_JSON, "timer": traffic_timer_JSON}

    return json.dumps(array_JSON, default=serialize)


def deserialize(lights_array_JSON):
    deserialized_JSON = []

    lights_array_JSON = json.loads(lights_array_JSON)

    # traffic_lights = lights_array_JSON['trafficlights']

    for i in range(len(lights_array_JSON)):
        deserialized_JSON.append([float(lights_array_JSON[i]['id']), lights_array_JSON[i]['weight']])

    return deserialized_JSON

class TrafficLights(object):
    def __init__(self):
        self.traffic_lights = []

    def __get__(self, instance, owner):
        return self.traffic_lights

    def __set__(self, instance, updated_lights_array):
        self.traffic_lights = updated_lights_array


class ReturnTrafficLights(object):
    traffic_lights = TrafficLights()

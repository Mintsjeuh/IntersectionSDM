class TrafficLights(object):
    def __init__(self):
        self.traffic_lights = []

    def __get__(self, instance, owner):
        print("GET traffic lights")
        return self.traffic_lights

    def __set__(self, instance, updated_lights_array):
        print("SET traffic lights")
        self.traffic_lights = updated_lights_array


class ReturnTrafficLights(object):
    traffic_lights = TrafficLights()

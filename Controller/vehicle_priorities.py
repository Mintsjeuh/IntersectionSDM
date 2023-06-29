import Controller.TrafficLights as traffic_lights

traffic_lights_array = traffic_lights.ReturnTrafficLights()

# check if priority is needed for the given id
def check(prio_id):
    for i in range(len(traffic_lights_array.traffic_lights)):
        if traffic_lights_array.traffic_lights[i].id == prio_id:
            if traffic_lights_array.traffic_lights[i].weight != 0:
                print("Prio for: ", prio_id)
                return True

    return False


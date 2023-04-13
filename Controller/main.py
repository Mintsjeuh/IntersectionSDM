import Controller.traffic_controller as controller
import Controller.socket_server as server

def main():
    controller.init_lights()
    server.run()


# run main method
if __name__ == "__main__":
    main()

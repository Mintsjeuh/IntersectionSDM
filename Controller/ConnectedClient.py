class ConnectedClient(object):
    def __init__(self):
        self.connected_client = []

    def __get__(self, instance, owner):
        print("GET client")
        return self.connected_client

    def __set__(self, instance, updated_connected_client):
        print("SET client")
        self.connected_client = updated_connected_client


class ReturnConnectedClient(object):
    connected_client = ConnectedClient()

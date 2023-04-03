import socketserver
import Controller.ConnectedClient as connected_client
import Controller.traffic_controller as controller
import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 11000

client = connected_client.ReturnConnectedClient()

class TCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for the server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        client = []
        # self.request is the TCP socket connected to the client
        client_connection = self.request
        client_address = self.client_address[0]

        client.append(client_connection)
        client.append(client_address)

        connected_client_array = connected_client.ReturnConnectedClient()
        connected_client_array.connected_client = client

        controller.handle_connection()


def receive(connection, client_address):
    received_bytes = connection.recv(2048).strip()
    received_string = received_bytes.decode('utf8')
    print("Received string from simulator at", client_address, received_string)
    return received_string


def send(data):
    # send the JSON-string to the client
    send_data = data
    send_bytes = send_data.encode(encoding='utf8')
    client.connected_client[0].sendall(send_bytes)

    print("Sent bytes to simulator: ", send_bytes)

def run():
    print("IP-address of server:", HOST)
    # Create the server, binding to HOST on PORT
    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        # Activate the server; this will keep running until you interrupt the program
        server.serve_forever()

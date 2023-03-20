import socketserver

HOST = "192.168.1.229"
PORT = 11000

class TCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for the server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        connection = self.request
        print("connection:", type(connection))
        client_address = self.client_address[0]
        print("address:", client_address)

        receive(connection, client_address)


def receive(connection, client_address):
    received_bytes = connection.recv(1024).strip()
    received_string = received_bytes.decode('utf8')
    print("Received string from simulator at", client_address, received_string)


def send():
    # send the JSON-string to the client
    send_data = '[{"id": 8.1, "status": 2}]'
    send_bytes = send_data.encode(encoding='utf8')
    TCPHandler.request.sendall(send_bytes)
    print("Sent bytes to simulator: ", send_bytes)

# if __name__ == "__main__":

def initialize():
    # Create the server, binding to HOST on PORT
    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        # Activate the server; this will keep running until you interrupt the program
        server.serve_forever()
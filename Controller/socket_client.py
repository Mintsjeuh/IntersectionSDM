import logging
import socket
import time
import socket

logging.basicConfig(level=logging.INFO)

HOST = socket.gethostbyname(socket.gethostname()) # The server's hostname or IP address.
PORT = 11000  # The port used by the server.

send_data = '[{"id": 42.0, "weight": 0},' \
            ' {"id": 1.1, "weight": 20},' \
            ' {"id": 2.1, "weight": 10},' \
            ' {"id": 5.1, "weight": 10},' \
            ' {"id": 6.1, "weight": 10},' \
            ' {"id": 7.1, "weight": 10},' \
            ' {"id": 8.1, "weight": 3},' \
            ' {"id": 9.1, "weight": 10},' \
            ' {"id": 10.1, "weight": 10},' \
            ' {"id": 11.1, "weight": 10},' \
            ' {"id": 12.1, "weight": 15}]'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        send_bytes = send_data.encode(encoding='utf8')
        s.sendall(send_bytes)

        time.sleep(3)

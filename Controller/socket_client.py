import logging
import socket
import time

logging.basicConfig(level=logging.INFO)

# HOST = "141.252.221.98"
HOST = "192.168.2.22"  # The server's hostname or IP address.
PORT = 11000  # The port used by the server.

send_data = '[{"id": 2.1, "weight": 20},' \
            ' {"id": 5.1, "weight": 10},' \
            ' {"id": 8.1, "weight": 3},' \
            ' {"id": 11.1, "weight": 15}]'


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        time.sleep(1)
        send_bytes = send_data.encode(encoding='utf8')
        s.sendall(send_bytes)

        data = s.recv(2048)

        if not data:
            break

        logging.info(f"Received {data!r}")
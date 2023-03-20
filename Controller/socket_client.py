import logging
import socket
import time

logging.basicConfig(level=logging.INFO)

HOST = "192.168.1.229"  # The server's hostname or IP address.
PORT = 11000  # The port used by the server.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        time.sleep(1)
        s.sendall(b"hello world")

        data = s.recv(1024)

        if not data:
            break

        logging.info(f"Received {data!r}")
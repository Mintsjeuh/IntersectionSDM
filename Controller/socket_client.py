import logging
import random
import time
import socket

logging.basicConfig(level=logging.INFO)

HOST = socket.gethostbyname(socket.gethostname())  # The server's hostname or IP address.
PORT = 11000  # The port used by the server.


def set_data():
    send_data = '[{"id": 42.0, "weight": ' + str(random.randint(0, 1)) + '},' \
                ' {"id": 1.1, "weight": ' + str(random.randint(0, 20)) + '},' \
                ' {"id": 2.1, "weight": ' + str(random.randint(0, 20)) + '},' \
                ' {"id": 5.1, "weight": ' + str(random.randint(0, 20)) + '},' \
                ' {"id": 6.1, "weight": ' + str(random.randint(0, 20)) + '},' \
                ' {"id": 7.1, "weight": ' + str(random.randint(0, 20)) + '},' \
                ' {"id": 8.1, "weight": ' + str(random.randint(0, 20)) + '},' \
                ' {"id": 9.1, "weight": ' + str(random.randint(0, 20)) + '},' \
                ' {"id": 10.1, "weight": ' + str(random.randint(0, 20)) + '},' \
                ' {"id": 11.1, "weight": ' + str(random.randint(0, 20)) + '},' \
                ' {"id": 12.1, "weight": ' + str(random.randint(0, 20)) + '},' \
                ' {"id": 35.1, "weight": ' + str(random.randint(0, 20)) + '},' \
                ' {"id": 35.2, "weight": ' + str(random.randint(0, 20)) + '},' \
                ' {"id": 36.1, "weight": ' + str(random.randint(0, 20)) + '},' \
                ' {"id": 36.2, "weight": ' + str(random.randint(0, 20)) + '},' \
                ' {"id": 86.1, "weight": ' + str(random.randint(0, 20)) + '},' \
                ' {"id": 26.1, "weight": ' + str(random.randint(0, 20)) + '},' \
                ' {"id": 37.2, "weight": ' + str(random.randint(0, 20)) + '},' \
                ' {"id": 37.1, "weight": ' + str(random.randint(0, 20)) + '},' \
                ' {"id": 38.1, "weight": ' + str(random.randint(0, 20)) + '},' \
                ' {"id": 38.2, "weight": ' + str(random.randint(0, 20)) + '},' \
                ' {"id": 88.1, "weight": ' + str(random.randint(0, 20)) + '},' \
                ' {"id": 28.1, "weight": ' + str(random.randint(0, 20)) + '},' \
                ' {"id": 31.2, "weight": ' + str(random.randint(0, 20)) + '},' \
                ' {"id": 31.1, "weight": ' + str(random.randint(0, 20)) + '},' \
                ' {"id": 32.1, "weight": ' + str(random.randint(0, 20)) + '},' \
                ' {"id": 32.2, "weight": ' + str(random.randint(0, 20)) + '},' \
                ' {"id": 22.0, "weight": ' + str(random.randint(0, 20)) + '}]'

    return send_data


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    send_data = set_data()
    send_bytes = send_data.encode(encoding='utf8')
    s.sendall(send_bytes)
    while True:
        if s.recv(2048).strip() is not None:
            send_data = set_data()
            send_bytes = send_data.encode(encoding='utf8')
            s.sendall(send_bytes)
        else:
            time.sleep(1)



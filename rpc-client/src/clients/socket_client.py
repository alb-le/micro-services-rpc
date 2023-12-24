import socket
from typing import Tuple


class SocketClient:
    def __init__(self, host: str,
                 port: int,
                 ):
        self.client: socket.socket = None
        self._server_address = (host, port)

    def get_socket(self):
        self.client: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_listening(self):
        self.client.bind(self.__address)
        self.client.listen()
        print(f'+ Server {self.__str__()} started.')

    def connect(self, address):
        self.client.connect(address)

    def accept(self) -> Tuple[socket.socket, Tuple[str, int]]:
        return self.client.accept()

    def close(self):
        self.client.close()

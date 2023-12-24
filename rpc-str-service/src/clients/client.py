import socket
from typing import Tuple


class Client:
    def __init__(self, host: str,
                 port: int,
                 ):
        self.server_client: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__address = (host, port)

    def __str__(self):
        return f'{self.__address[0]}:{self.__address[1]}'

    def start_listening(self):
        self.server_client.bind(self.__address)
        self.server_client.listen()
        print(f'+ Server {self.__str__()} started.')

    def accept(self) -> Tuple[socket.socket, Tuple[str, int]]:
        return self.server_client.accept()

    def close(self):
        self.server_client.close()

import json

import config
from src.clients.socket_client import SocketClient


class Client(SocketClient):
    def __init__(self, host: str, port: int):
        super().__init__(host, port)

    def __str__(self):
        return f'{self._server_address[0]}:{self._server_address[1]}'

    def handshake(self):
        self.get_socket()
        self.connect(self._server_address)

    def call_fn(self, fn_name, args, kwargs):
        self.client.sendall(json.dumps((fn_name, args, kwargs)).encode())
        res = self.client.recv(config.MSG_SIZE).decode()
        return json.loads(res)

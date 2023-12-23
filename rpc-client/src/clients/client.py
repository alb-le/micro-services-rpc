import json

import config
from src.clients.socket_client import SocketClient


class Client(SocketClient):
    def __init__(self, host: str, port: int):
        super().__init__(host, port)
        self.server_address = (host, config.SERVER_PORT)

    def handshake(self):
        adds = self.server_address
        print(f'server address: {adds}')
        self.socket.connect(self.server_address)

    def call_fn(self, fn_name, args, kwargs):
        self.socket.sendall(json.dumps((fn_name, args, kwargs)).encode())
        res = self.socket.recv(config.MSG_SIZE).decode()
        return json.loads(res)

from typing import Tuple, Optional

import config
from src.clients.client_client import ClientClient
from src.rcp_client import RcpClient


def client_handler():
    host = config.HOST
    port = config.PORT

    client = ClientClient(host, port)
    RcpClient(client=client).run()


if __name__ == "__main__":
    client_handler()

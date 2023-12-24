
from src.rcp_client import RcpClientController
from src.clients.client import Client
import config

def client_handler():
    client = Client(config.HOST, config.SERVER_PORT)
    rpc_client = RcpClientController(client=client)
    while True:
        user_input = get_input()
        res = rpc_client.run(user_input)
        if not res:
            break
        print(res)

def get_input() -> str:
    return input(f'Write a request. You might try "help()" or "exit():"')

if __name__ == "__main__":
    client_handler()

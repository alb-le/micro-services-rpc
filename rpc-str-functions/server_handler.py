import config
from src.clients.server_client import ServerClient
from src.server_functions import FunctionsImplementation
from src.rpc_server import RpcServer


def server_handler():
    client = ServerClient(host=config.HOST, port=config.PORT)
    fn = FunctionsImplementation()
    RpcServer(client=client, my_functions=fn).run()


if __name__ == "__main__":
    server_handler()

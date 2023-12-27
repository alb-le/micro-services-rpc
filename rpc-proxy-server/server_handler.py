import config
from src.clients.server_client import ServerClient
from src.services_signatures import ServicesSignatures
from src.rpc_server import RpcServer
from src.cache_controller import CacheController


def server_handler():
    client = ServerClient(host=config.HOST, port=config.PORT)
    cache = CacheController(host=config.CACHE_HOST, port=config.CACHE_PORT)
    services = ServicesSignatures(cache=cache)
    RpcServer(client=client, services=services).run()


if __name__ == "__main__":
    server_handler()

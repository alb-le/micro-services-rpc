import os
import socket


def get_host_name(name, otherwise):
    try:
        host = socket.gethostbyname(name)
    except socket.gaierror:
        print(f"[ERROR] No host with name {name}")
        host = otherwise
    print(f"[INFO] Server host_name: {host}")
    return host


MSG_SIZE: int = int(os.getenv("MSG_SIZE", 1024))
HOST: str = os.getenv("HOST", "0.0.0.0")
PORT: int = int(os.getenv("PORT", 5051))
SERVER_PORT: int = int(os.getenv("SERVER_PORT", 5051))

NUM_SERVICE_HOST: str = os.getenv(
    "NUM_SERVICE_HOST", get_host_name("num-service", "localhost")
)
NUM_SERVICE_PORT: int = int(os.getenv("NUM_SERVICE_PORT", 5052))

STR_SERVICE_HOST: str = os.getenv(
    "STR_SERVICE_HOST", get_host_name("str-service", "localhost")
)
STR_SERVICE_PORT: int = int(os.getenv("STR_SERVICE_PORT", 5053))

CACHE_HOST: str = os.getenv("CACHE_HOST", get_host_name("redis-cache", "localhost"))
CACHE_PORT: int = int(os.getenv("CACHE_PORT", 6379))

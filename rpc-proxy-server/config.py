import os
import socket

def get_host_name(name, otherwise):
    try:
        return socket.gethostbyname(name)
    except socket.gaierror:
        return otherwise

MSG_SIZE:int = int(os.getenv('MSG_SIZE', 1024))
HOST:str = os.getenv('HOST', '0.0.0.0')
PORT: int = int(os.getenv('PORT', 5051))
SERVER_PORT: int = int(os.getenv('SERVER_PORT', 5051))

NUM_SERVICE_HOST: str = os.getenv('NUM_SERVICE_HOST', get_host_name('rpc-num-service', 'localhost'))
NUM_SERVICE_PORT: int = int(os.getenv('NUM_SERVICE_PORT', get_host_name('rpc-num-service', 5052)))

NUM_SERVICE_HOST: str = os.getenv('STR_SERVICE_HOST', get_host_name('rpc-str-service', 'localhost'))
STR_SERVICE_PORT: int = int(os.getenv('STR_SERVICE_PORT', get_host_name('rpc-str-service', 5053)))

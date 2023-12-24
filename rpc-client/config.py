import os
import socket

def get_host_name(name):
    try:
        return socket.gethostbyname(name)
    except socket.gaierror:
        return '127.0.0.1'

MSG_SIZE:int = int(os.getenv('MSG_SIZE', 1024))
HOST:str = os.getenv('HOST', get_host_name('rpc-proxy-server'))
PORT: int = int(os.getenv('PORT', 5050))
SERVER_PORT: int = int(os.getenv('SERVER_PORT', 5051))

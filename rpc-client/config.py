import os
import socket

def get_host_name(name):
    try:
        host = socket.gethostbyname(name)
    except socket.gaierror:
        print(f'[ERROR] No host with name {name}')
        host = '127.0.0.1'
    print(f'[INFO] Server host_name: {host}')
    return host

MSG_SIZE:int = int(os.getenv('MSG_SIZE', 1024))
HOST:str = os.getenv('HOST', get_host_name('proxy-server'))
PORT: int = int(os.getenv('PORT', 5050))
SERVER_PORT: int = int(os.getenv('SERVER_PORT', 5051))

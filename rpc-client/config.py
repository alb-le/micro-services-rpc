import os

MSG_SIZE:int = int(os.getenv('MSG_SIZE', 1024))
HOST:str = os.getenv('', '127.0.0.1')
PORT: int = int(os.getenv('PORT', 5050))
SERVER_PORT: int = int(os.getenv('SERVER_PORT', 5051))

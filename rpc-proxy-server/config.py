import os

MSG_SIZE:int = int(os.getenv('MSG_SIZE', 1024))
HOST:str = os.getenv('', '127.0.0.1')
PORT: int = int(os.getenv('PORT', 5051))
SERVER_PORT: int = int(os.getenv('SERVER_PORT', 5051))
NUM_SERVICE_PORT: int = int(os.getenv('NUM_SERVICE_PORT', 5052))
STR_SERVICE_PORT: int = int(os.getenv('STR_SERVICE_PORT', 5053))

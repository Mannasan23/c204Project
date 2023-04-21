import socket
from threading import Thread

SERVER = None
PORT = 6000
IP_ADDRESS = '127.0.0.1'
CLIENTS = {}

def setup():
    print("\n\t\t\t\t\t*** Welcome to Tambola Game ***\n")

    global SERVER
    global PORT
    global IP_ADDRESS


    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(10)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMING CONNECTIONS...\n")

setup()
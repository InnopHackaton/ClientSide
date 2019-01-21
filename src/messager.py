#!/usr/bin/python3
"""Script for chat client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from coder import Encoder, Decoder
from time import sleep
import configparser
import sys


def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ)
            sys.stdout.write(decoder.decode(msg))
        except OSError:  # Possibly client has left the chat.
            break


def send():
    """Handles sending of messages."""
    while True:
        msg = sys.stdin.readline()
        client_socket.send(encoder.encode(msg))


encoder, decoder = Encoder(), Decoder()
config = configparser.ConfigParser()
config.read('configs/config.ini')

# ----Now comes the sockets part----
HOST, PORT = config['DEFAULT']['SERVER_IP'], int(config['DEFAULT']['MES_PORT'])

BUFSIZ = 6144
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

Thread(target=receive).start()
sleep(1)
Thread(target=send).start()

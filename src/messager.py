#!usr/bin/python3.6
import select
import socket
import sys
import threading
from coder import Encoder, Decoder

def promt():
    sys.stdout.write("<YOU>:")
    sys.stdout.flush()

def recv_message(socket):
    while True:
        read_socket, write_socket, error_socket = select.select([socket], [], [])

        if len(read_socket) >= 1:
            try:
                message = read_socket[0].recv(1024).decode("utf-8")
                sys.stdout.write(message)
            except Exception as e:
                print("Can't received ", e)


def send_message(socket):
    while True:
        message = sys.stdin.readline()
        try:
            socket.send(encoder.encode(message))
            promt()
        except Exception as e:
            sys.stdout.write(e)
            sys.exit(1)


if __name__ == "__main__":
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.settimeout(2)
    encoder, decoder = Encoder(), Decoder()

    try:
        socket.connect(("80.211.104.94", 1337))
    except Exception as e:
        print("Connection failed: ", e)
        sys.exit(1)
    
    promt()
    threading.Thread(target=send_message, args=(socket,)).start()
    threading.Thread(target=recv_message, args=(socket,)).start()

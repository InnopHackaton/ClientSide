#!/usr/bin/python3
import select
import socket
import sys
import threading
import gnupg

def recv_message(socket):
    read_socket, write_socket, error_socket = select.select([socket], [], [])

    if len(read_socket) >= 1:
        try:
            message = read_socket[0].recv(2 ** 13)
            gpg = gnupg.GPG(gnupghome='/home/hackathon/.gnupg')
            result = gpg.import_keys(message)
            print(result.results)
        except Exception as e:
            print("Can't received ", e)


def send_message(socket):
    message = sys.stdin.readline()
    try:
        socket.send(message.encode("utf-8"))
    except:
        sys.stdout.write("\rError message")
        sys.exit(1)


if __name__ == "__main__":
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.settimeout(2)

    try:
        socket.connect(("80.211.104.94", 1338))
    except Exception as e:
        print("Connection failed: ", e)
        sys.exit(1)

    send_message(socket)
    recv_message(socket)

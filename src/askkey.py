#!/usr/bin/python3
import select
import socket
import sys
import gnupg
import configparser

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

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('configs/config.ini')
    HOST, PORT = config['DEFAULT']['SERVER_IP'], config['DEFAULT']['KEY_PORT']

    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.settimeout(2)
    
    try:
        socket.connect((HOST, int(PORT)))
    except Exception as e:
        print("Connection failed: ", e)
        sys.exit(1)

    recv_message(socket)

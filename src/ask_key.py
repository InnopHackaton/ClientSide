import socket

s = socket.socket()
host = "80.211.104.94"
port = 1338

s.connect((host, port))
data = s.recv(2**13)
w = open("pub_key.asc", "w")
w.write(data)



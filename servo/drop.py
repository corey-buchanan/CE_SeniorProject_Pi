import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.15', 9001))

s.send(bytes("Drop", "utf-8"))

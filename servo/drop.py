# Used to test the servo socket server - not used in production
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('172.20.10.6', 9001))

s.send(bytes("Drop\n", "utf-8"))

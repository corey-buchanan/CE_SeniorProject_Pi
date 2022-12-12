from gpiozero import Servo
import time
import socket
import selectors
import sys
import types

# Credit to https://realpython.com/python-sockets/#handling-multiple-connections for instruction on how to service multiple
# socket connections.

def accept_wrapper(sock):
  conn, addr = sock.accept()
  print(f"Accepted connectionfrom {addr}")
  conn.setblocking(False)
  data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
  events = selectors.EVENT_READ | selectors.EVENT_WRITE
  sel.register(conn, events, data=data)

def handle_connection(key, mask):
  sock = key.fileobj
  data = key.data
  if mask & selectors.EVENT_READ:
    msg = sock.recv(10).decode("utf-8")
    if msg:
      if msg == "Load\n":
        servo.max()
      elif msg == "Drop\n":
        servo.min()
    else:
      print(f"Closing connection to {data.addr}")
      sel.unregister(sock)
      sock.close()

if len(sys.argv) < 2:
  print("Please specify a port!")
  exit(1)

sel = selectors.DefaultSelector()

host, port = '', int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

servo = Servo(17)
servo.min()

s.listen()
print(f"Listening on {(host, port)}")
s.setblocking(False)

sel.register(s, selectors.EVENT_READ, data=None)

try:
  while True:
    events = sel.select(timeout=None)
    for key, mask in events:
      if key.data is None:
        accept_wrapper(key.fileobj)
      else:
        handle_connection(key, mask)
finally:
  sel.close()

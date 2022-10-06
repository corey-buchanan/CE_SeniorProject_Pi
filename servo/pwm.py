import RPi.GPIO as GPIO
import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.0.15', 9001))

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM
p.start(2.5) # Initialization

s.listen(5)

try:
  while True:
    conn, address = s.accept()
    msg = conn.recv(10).decode("utf-8")
    if msg == "Load":
      p.ChangeDutyCycle(2.5)
    elif msg == "Drop":
      p.ChangeDutyCycle(12.5)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()

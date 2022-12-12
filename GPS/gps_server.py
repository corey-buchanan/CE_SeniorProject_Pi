# Thanks to Adafruit for the tutorial provided with their GPS module

import socket

# Simple GPS module demonstration.
# Will wait for a fix and print a message every second with the current location
# and other details.
import time
import board
import busio
import adafruit_gps

# Create a serial connection for the GPS connection using default speed and
# a slightly higher timeout (GPS modules typically update once a second).

import serial
uart = serial.Serial("/dev/serial0", baudrate=9600, timeout=10)

# Create a GPS module instance.
gps = adafruit_gps.GPS(uart, debug=False)  # Use UART/pyserial

# Turn on the basic GGA and RMC info 
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")

# Set update rate to once a second (1hz) 
gps.send_command(b"PMTK220,1000")

def getCoordinates():
    gps.update()
    
    if not gps.has_fix:
        # Spoof a random location to send to the client in the case the gps doesn't have a fix
        # this happens in areas where the GPS doesn't work well, such as in a large building
        # or on school campus.
        latitude = "41.0325501"
        longitude = "-111.95833025"
    else:
        latitude = "{0:.7f}".format(gps.latitude)
        longitude = "{0:.7f}".format(gps.longitude)

    coordinates = str(latitude)+ "," + str(longitude)
    print("Coordinates",coordinates)

    return(coordinates)

HOST = ''
PORT = 8081

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    while True:
        s.listen()
        conn, addr = s.accept()
        with conn: 
            print(f"Connected by {addr}")
            
            coordinates = getCoordinates()
            conn.sendall(coordinates.encode())

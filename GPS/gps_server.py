import socket
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

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
# gps = adafruit_gps.GPS_GtopI2C(i2c, debug=False)  # Use I2C interface

# Initialize the GPS module by changing what data it sends and at what rate.

# Turn on the basic GGA and RMC info 
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")

# Set update rate to once a second (1hz) 
gps.send_command(b"PMTK220,1000")

def getCoordinates():
    # Make sure to call gps.update() every loop iteration and at least twice
    # as fast as data comes from the GPS unit (usually every second).
    # This returns a bool that's true if it parsed new data (you can ignore it
    # though if you don't care and instead look at the has_fix property).
    gps.update()
    # Every second print out current location details if there's a fix.
    
    if not gps.has_fix:
        latitude = "41.0325501"
        longitude = "-111.95833025"
    else:
        latitude = "{0:.7f}".format(gps.latitude)
        longitude = "{0:.7f}".format(gps.longitude)

    coordinates = str(latitude)+ "," + str(longitude)
    print("Coordinates",coordinates)

    return(coordinates)

HOST = '169.254.221.209'  # Standard loopback interface address (localhost)
PORT = 8081  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    while True:
        s.listen()
        conn, addr = s.accept()
        with conn: 
            print(f"Connected by {addr}")
            
            coordinates = getCoordinates()
            conn.sendall(coordinates.encode())

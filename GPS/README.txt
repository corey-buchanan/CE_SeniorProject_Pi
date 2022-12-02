To get the GPS to work you need to make the following installs

sudo pip3 install adafruit-blinka
sudo pip3 install adafruit-circuitpython-gps

You may also need to disable login by shell in the interface option at
sudo raspi-config


Also, make sure to follow the following PINOUT

VIN - 3.3v (1)
GND - GND (6)
RX - TX (8)
TX - RX (10)

#!/bin/bash

service dhcpcd stop
sleep 5
service hostapd stop
sleep 5
service hostapd start
sleep 5
service dhcpcd start

python3 /home/drone/drone/video_stream/stream_server.py &

python3 /home/drone/drone/servo/servo_ctrl.py 8001 &

python3 /home/drone/drone/GPS/gps_server.py &

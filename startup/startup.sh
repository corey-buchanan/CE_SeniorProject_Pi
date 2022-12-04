#!/bin/bash

service dhcpcd stop
sleep 5
service hostapd stop
sleep 5
service hostapd start
sleep 5
service dhcpcd start

sleep 10
# raspivid -n -t 0 -w 1280 -h 720 -ih -fps 24 -fl -o - | nc -lkv4 8080 &
python3 /home/drone/drone/video_stream/stream_server.py &

python3 /home/drone/drone/servo/servo_ctrl.py 8001 &

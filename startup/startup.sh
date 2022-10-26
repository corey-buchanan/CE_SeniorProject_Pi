#!/bin/bash

sleep 10
# raspivid -n -t 0 -w 1280 -h 720 -ih -fps 24 -fl -o - | nc -lkv4 8080 &
python3 /home/drone/drone/video_stream/stream_server.py &

python3 /home/drone/drone/servo/servo_ctrl.py 8001 &

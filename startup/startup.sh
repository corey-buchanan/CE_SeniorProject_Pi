#!/bin/bash

sleep 5
raspivid -n -t 0 -w 1280 -h 720 -ih -fps 24 -fl -o - | nc -lkv4 8080

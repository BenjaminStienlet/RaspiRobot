#!/bin/bash

# This script starts mjpg-streamer and the main python script.

mjpg_folder="./mjpg-streamer-raspicam"

echo "mjpg-streamer started"
LD_LIBRARY_PATH=$mjpg_folder $mjpg_folder/mjpg_streamer -i "input_raspicam.so -x 640 -y 480 -fps 15 -vf -hf" -o "output_http.so -p 9000 -w $mjpg_folder/www" &
sleep 4

echo ""
echo "python script started"
python -m raspi_robot
echo "python script stopped"

kill $(pidof mjpg_streamer)
echo "mjpg-streamer stopped"

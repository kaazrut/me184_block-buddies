#! /bin/sh
# launcher.sh
# navigate to the block-buddies dir, then execute the main python script

amixer set PCM -- -1000
cd /
cd home/pi/me184_block-buddies
sudo python main.py
cd /

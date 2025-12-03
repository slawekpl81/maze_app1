#!/bin/bash
xhost +local:docker

docker run -it --rm \
  -v "$(pwd)":/app -w /app \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v $XAUTHORITY:/root/.Xauthority:ro -e XAUTHORITY=/root/.Xauthority \
  --net=host --ipc=host --device /dev/snd \
  fedora-py-raylib bash
#!/bin/bash

docker build -t server .

docker run -it --rm --name server \
-p 9090:9090 \
-v .:/code \
server

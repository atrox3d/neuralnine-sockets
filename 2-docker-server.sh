#!/bin/bash

docker build -f dockerfile-server -t server .

docker run -it --rm --name server \
-p 9090:9090 \
-v .:/code \
--net socketnet \
--hostname server \
server

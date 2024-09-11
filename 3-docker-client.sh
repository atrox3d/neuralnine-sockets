#!/bin/bash

docker build -f dockerfile-client -t client .

docker run -it --rm --name client \
-v .:/code \
--net socketnet \
client

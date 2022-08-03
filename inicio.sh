#!/bin/bash

sudo apt-get -y install screen

docker build -t display .

#screen -S docker -d -m bash -c "docker run -it --rm -v $PWD/img:/app/Almacenamiento/img display"
#screen -S dockercompose -d -m bash -c "sudo docker-compose build && sudo docker-compose up -d"

#screen -S web -d -m bash -c "cd img/ && python3 -m http.server 8080"

screen -S docker -d -m bash -c "docker run -it --rm -v $PWD/img:/app/Almacenamiento/img display"
screen -S web -d -m bash -c "cd img/ && python3 -m http.server 8080"

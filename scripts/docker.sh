#!/usr/bin/env bash

. ~/.bashrc

env SFIA2_DB_URI="${SFIA2_DB_URI}" 

env SECRET_KEY="${SECRET_KEY}"

docker-compose build

docker push hamzay97/sfia2_service_1:latest

docker push hamzay97/sfia2_service_2:latest

docker push hamzay97/sfia2_service_3:latest

docker push hamzay97/sfia2_service_4:latest

docker stack deploy --compose-file docker-compose.yaml stack1
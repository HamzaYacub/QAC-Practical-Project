#!/usr/bin/env bash

. ~/.bashrc

env SFIA2_DB_URI="${SFIA2_DB_URI}" 

env SECRET_KEY="${SECRET_KEY}"

docker stack deploy --compose-file docker-compose.yaml stack1
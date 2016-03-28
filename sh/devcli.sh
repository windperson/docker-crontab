#!/bin/bash

set -x
docker-compose -f docker-compose.base.yml build
docker-compose -f docker-compose.dev.yml build
docker-compose -f docker-compose.dev.yml run --rm --name dev-cli cron-serv-dev-cli
exit

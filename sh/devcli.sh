#!/bin/bash

base_yml=docker-compose.python3.base.yml

if [ -z $PYTHON_VER ]
then
    base_yml=docker-compose.python3.base.yml
else
    base_yml=docker-compose.python${PYTHON_VER}.base.yml
fi

set -x
docker-compose -f $base_yml build
docker-compose -f docker-compose.dev.yml build
docker-compose -f docker-compose.dev.yml run --rm --name dev-cli cron-serv-dev-cli
exit

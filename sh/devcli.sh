#!/bin/bash

base_yml=docker-compose.python3.base.yml

while getopts "hb" arg; do
    case $arg in
      h)
        echo ""
        echo "usage: [-h] [-b build but not run]"
        echo ""
        exit
        ;;
      b)
        build_only=true
        ;;
    esac
done


if [ -z $PYTHON_VER ]
then
    base_yml=docker-compose.python3.base.yml
else
    base_yml=docker-compose.python${PYTHON_VER}.base.yml
fi

set -x
docker-compose -f ${base_yml} build
docker-compose -f docker-compose.dev.yml build
if [ -z $build_only ]
then
    docker-compose -f docker-compose.dev.yml run --rm --name dev-cli cron-serv-dev-cli
fi
exit

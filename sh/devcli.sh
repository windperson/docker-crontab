#!/bin/bash

base_yml=docker-compose.python3.base.yml

build_only=false

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
source ./sh/build_base_image.sh && docker-compose -f docker-compose.dev.yml build
if [ "$build_only" = false ]
then
echo "enter dev cli:"
    docker-compose -f docker-compose.dev.yml run --rm --name dev-cli cron-serv-dev-cli
fi

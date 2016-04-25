#!/bin/bash

base_yml=docker-compose.python3.base.yml

while getopts "hc:f:rn" arg; do
    case $arg in
      h)
        echo ""
        echo "usage: [-h] [-n => always pull new image] [-r => Always remove intermediate result]"
        echo ""
        exit
        ;;
      r)
        ForceRmArg="--force-rm"
        ;;
      n)
        AlwayPullArg="--pull"
        ;;
    esac
done


if [ -z $PYTHON_VER ]
then
    base_yml=docker-compose.python3.base.yml
else
    base_yml=docker-compose.python${PYTHON_VER}.base.yml
fi

auxArg=""
if [ ! -z "${ForceRmArg}" ]
then
     auxArg="${ForceRmArg}"
fi

if [ ! -z "${AlwayPullArg}" ]
then
     auxArg="${auxArg} ${AlwayPullArg}"
fi

set -x
docker-compose -f ${base_yml} build ${auxArg}
set +x

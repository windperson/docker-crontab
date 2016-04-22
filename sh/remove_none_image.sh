#!/bin/bash

while getopts "ha" arg; do
    case $arg in
      h)
        echo ""
        echo "usage: [-h] [-a clear_all]"
        echo ""
        exit
        ;;
      a)
        clear_all=true
        ;;
    esac
done

if [ -z $clear_all ]
then
  set -e
  docker rmi -f $(docker images -aq -f=dangling=true)
  set +e
else
  set -e
  docker rmi -f $(docker images -aq)
  set +e
fi
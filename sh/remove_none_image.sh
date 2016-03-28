#!/bin/bash
set -x
docker rmi -f $(docker images -q -f=dangling=true)
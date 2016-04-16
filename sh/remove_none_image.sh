#!/bin/bash
docker rmi -f $(docker images -aq -f=dangling=true)
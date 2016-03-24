#!/bin/bash

set -x
docker-compose -f docker-compose.dev.yml run cron-serv-dev-cli
exit

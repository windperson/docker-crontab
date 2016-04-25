#!/bin/bash

exec circusd --log-level ${CIRCUS_LOG_LEVEL} /etc/circus/circus.ini

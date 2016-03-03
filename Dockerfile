FROM python:3-slim
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y apt-utils g++ less libzmq-dev libevent-dev
RUN pip install --upgrade pip setuptools
RUN pip install apscheduler croniter python-crontab ipython
ARG PROJ_SRC_DIR
ENV PROJ_SRC_DIR ${PROJ_SRC_DIR:-/proj}
ARG PROJ_CONF_DIR
ENV PROJ_CONF_DIR ${PROJ_CONF_DIR:-/conf}
WORKDIR ${PROJ_SRC_DIR}
VOLUME ${PROJ_SRC_DIR}
VOLUME ${PROJ_CONF_DIR}
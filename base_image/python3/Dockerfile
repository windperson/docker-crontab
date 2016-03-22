FROM python:3-slim
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y apt-utils g++ less libzmq-dev libevent-dev python-dev
RUN pip install --no-cache-dir --upgrade pip setuptools
ONBUILD ADD PROJ_SRC_DIR
ONBUILD ENV PROJ_SRC_DIR ${PROJ_SRC_DIR:-/proj}
ONBUILD ADD PROJ_CONF_DIR
ONBUILD ENV PROJ_CONF_DIR ${PROJ_CONF_DIR:-/conf}
ONBUILD WORKDIR ${PROJ_SRC_DIR}
ONBUILD VOLUME ${PROJ_SRC_DIR}
ONBUILD VOLUME ${PROJ_CONF_DIR}
ONBUILD RUN pip install --no-cache-dir -r requirements.txt
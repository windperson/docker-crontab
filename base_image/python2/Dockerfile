FROM python:2-slim
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y apt-utils g++ less libzmq-dev libevent-dev python-dev && apt-get clean
RUN pip install --no-cache-dir --upgrade pip setuptools
ONBUILD ARG PIP_REQUIRE_DIR
ONBUILD COPY ${PIP_REQUIRE_DIR}/requirements.txt /tmp/
ONBUILD RUN pip install --no-cache-dir -r /tmp/requirements.txt
ONBUILD ARG PROJ_SRC_DIR
ONBUILD ENV PROJ_SRC_DIR ${PROJ_SRC_DIR:-/proj}
ONBUILD ARG PROJ_CONF_DIR
ONBUILD ENV PROJ_CONF_DIR ${PROJ_CONF_DIR:-/conf}
ONBUILD WORKDIR ${PROJ_SRC_DIR}
ONBUILD VOLUME ${PROJ_SRC_DIR}
ONBUILD VOLUME ${PROJ_CONF_DIR}
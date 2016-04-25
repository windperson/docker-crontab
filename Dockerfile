FROM python3-base
MAINTAINER Charles Pao "windperson@gmail.com"
ARG TZ
ENV TZ=${TZ:-Asia/Taipei}
RUN pip install --no-cache-dir circus
COPY production_conf /etc/circus
COPY src /src
VOLUME /conf
CMD [ "sh", "-c", "circusd", "--log-level", "${CIRCUS_LOG_LEVEL}", "/etc/circus/circus.ini"]

FROM python2-base
MAINTAINER Charles Pao "windperson@gmail.com"
ARG TZ
ENV TZ=${TZ:-Asia/Taipei}
RUN pip install --no-cache-dir circus
COPY production_conf /etc/circus
COPY src /proj
VOLUME /conf
ENTRYPOINT [ "sh", "-c" "circusd" "--log-level" "${CIRCUS_LOG_LEVEL}" "/etc/circus/circus.ini"]
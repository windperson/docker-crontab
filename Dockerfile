FROM python3-base
ARG TZ
ENV TZ=${TZ:-Asia/Taipei}
RUN pip install --no-cache-dir circus
COPY src /proj
COPY production_conf /conf
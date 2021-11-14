FROM python:3.8-alpine

COPY app/ /app
WORKDIR /app
RUN pip install -r requirements.txt

USER root
COPY root /var/spool/cron/crontabs/

CMD crond -l 1 -f

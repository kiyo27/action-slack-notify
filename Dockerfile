FROM python:3.9.5-slim-buster

COPY src /usr/app
COPY entrypoint.sh /entrypoint.sh

RUN pip install -r /usr/app/requirements.txt \
    && chmod +x /*.sh

ENTRYPOINT ["/entrypoint.sh"]
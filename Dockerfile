FROM python:3.7-slim

LABEL maintainer="ysde108@gmail.com"

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app
RUN chown 65534:65534 .
COPY --chown=65534 . .

USER 65534

ENTRYPOINT ["./docker_entry.sh"]

# Run the web service on container startup.# https://hub.docker.com/_/python
FROM python:3.7-slim

# Copy local code to the container image.
ENV APP_ROOT /app
WORKDIR $APP_ROOT

COPY ./requirements.txt $APP_ROOT

RUN set -ex &&\
    apt-get update &&\
    apt-get install -y wget

RUN pip3 install -U -r /app/requirements.txt

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 main:app --reload

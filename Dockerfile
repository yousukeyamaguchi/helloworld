FROM python:3.7-slim

ENV APP_ROOT /app
WORKDIR $APP_ROOT

COPY ./src $APP_ROOT

RUN set -ex &&\
    pip install -r requirements.txt &&\
    pip install gunicorn

# Install production dependencies.
RUN pip install Flask gunicorn

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 main:app

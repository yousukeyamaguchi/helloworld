FROM python:3.7-slim

ENV APP_ROOT /app
WORKDIR $APP_ROOT

COPY ./src $APP_ROOT

RUN set -ex &&\
    pip install -r requirements.txt &&\
    pip install gunicorn &&\
    pip install Flask gunicorn

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 main:app

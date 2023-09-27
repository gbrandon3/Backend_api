FROM python:3.10-alpine

ENV TZ=America/Bogota 
ENV MINUTES_TOKEN_VEN=5

RUN mkdir -p /home/app
WORKDIR /home/app

COPY requirements.txt ./

RUN apk update \    
    && apk add postgresql-dev \
    && apk add gcc \
    && apk add python3-dev \
    && apk add musl-dev \
    && apk add py3-pip

RUN pip install psycopg2 \
    && pip install --no-cache-dir -r requirements.txt

COPY ./src ./

RUN adduser -S remote_user
USER remote_user

EXPOSE 5000

CMD [ "gunicorn", "--bind", "0.0.0.0:5002", "wsgi:app" ]
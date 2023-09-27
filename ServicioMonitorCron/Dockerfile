FROM python:3.10-alpine

ENV TZ=America/Bogota 
ENV MINUTES_TOKEN_VEN=5

RUN mkdir -p /home/app
WORKDIR /home/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./

RUN adduser -S remote_user
USER remote_user

CMD [ "python3", "App.py" ]
FROM python:3.6-slim
MAINTAINER Antonio Royo "antonio.royo@outlook.com"
RUN apt-get update -y
RUN apt-get install -y python3-dev build-essential \
    libxft-dev libfreetype6 libfreetype6-dev

COPY . /srv/flask_app
WORKDIR /srv/flask_app

RUN apt-get -y install nginx \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential

RUN pip install -r requirements.txt --src /usr/local/src

COPY nginx.conf /etc/nginx
RUN chmod +x ./start.sh
CMD ["./start.sh"]



FROM debian:9.5

RUN apt-get update
RUN apt-get install python3 python3-setuptools git python3-dev postgresql python3-pip -y

WORKDIR /app

COPY ./ /app

RUN pip3 install -r requirements/dev.txt

EXPOSE 8000

RUN python3 manage.py migrate

CMD python3 manage.py runserver 0.0.0.0:8000

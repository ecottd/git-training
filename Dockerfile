from ubuntu:18.04

RUN apt-get update -y && \
  apt-get install -y python3-pip python-dev
  
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "hello-world-flask.py" ]

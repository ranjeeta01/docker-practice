FROM ubuntu

RUN apt-get update

RUN apt-get install -y python

RUN apt-get install python-pip

RUN pip install flask

COPY simple-webapp /opt/simple-webapp

ENTRYPOINT FLASK_APP=/opt/simple-webapp/app.py flask run -host=0.0.0.0

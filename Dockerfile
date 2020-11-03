FROM python:3.8

WORKDIR /opt/myapp

COPY . /opt/myapp

RUN pip install -r requirements.txt

ENTRYPOINT ["/bin/bash", "start.sh"]

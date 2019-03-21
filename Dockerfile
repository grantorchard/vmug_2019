from ubuntu 

LABEL maintainer "Cody De Arkand <cdearkland@vmware.com>"
LABEL description "Simple API Image"

RUN apt update && apt install -y \
    git \
    python3.6 \
    python3-pip

RUN pip3 install requests flask

COPY app.py app.py

EXPOSE 80/tcp

ENTRYPOINT [ "/usr/bin/python3", "app.py" ]
FROM ubuntu:latest
RUN apt update && apt install -y python3
RUN set -xe \
    && apt-get update \
    && apt-get install -y python3-pip
RUN pip install --upgrade pip
WORKDIR /rpc-proxy-server
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 51
CMD python3 server_handler.py

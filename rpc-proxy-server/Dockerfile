FROM ubuntu:latest
RUN apt update && apt install -y python3
RUN apt install redis
WORKDIR /rpc-proxy-server
COPY . .
EXPOSE 51

CMD python3 server_handler.py

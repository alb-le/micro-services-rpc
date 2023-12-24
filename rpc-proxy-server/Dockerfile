FROM ubuntu:latest
RUN apt update && apt install -y python3
WORKDIR /rpc-proxy-server
COPY . .
EXPOSE 5051
CMD python3 server_handler.py

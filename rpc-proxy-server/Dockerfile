FROM ubuntu:latest
RUN apt update && apt install -y python3
EXPOSE 8081:8081
COPY . /rpc-proxy
CMD python3 ./rpc-proxy/server_handler.py

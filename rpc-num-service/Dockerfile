FROM ubuntu:latest
RUN apt update && apt install -y python3
WORKDIR /rpc-num-service
COPY . .
EXPOSE 52
CMD python3 server_handler.py

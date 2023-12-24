FROM ubuntu:latest
RUN apt update && apt install -y python3
WORKDIR /rpc-client
COPY . .
EXPOSE 5050:5050

FROM ubuntu:latest
RUN apt update && apt install -y python3
WORKDIR /rpc-client
COPY . .
EXPOSE 5050:5050
# CMD python3 ./rpc-client/client_handler.py

FROM ubuntu:latest
RUN apt update && apt install -y python3
EXPOSE 8080:8080
COPY . /rpc-client
CMD python3 ./rpc-client/client_handler.py

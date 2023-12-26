FROM ubuntu:latest
RUN apt update && apt install -y python3
WORKDIR /rpc-str-service
COPY . .
EXPOSE 53
CMD python3 server_handler.py

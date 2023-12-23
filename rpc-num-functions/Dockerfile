FROM ubuntu:latest
RUN apt update && apt install -y python3
EXPOSE 8082:8082
COPY . /rpc-num-fn
CMD python3 ./rpc-num-fn/server_handler.py

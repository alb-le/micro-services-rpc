FROM ubuntu:latest
RUN apt update && apt install -y python3
EXPOSE 8083:8083
COPY . /rpc-str-fn
CMD python3 ./rpc-str-fn/server_handler.py

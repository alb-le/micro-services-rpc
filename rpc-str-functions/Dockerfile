FROM ubuntu:latest
RUN apt update && apt install -y python3
WORKDIR /rpc-str-fn
COPY . .
EXPOSE 5053:5053
CMD python3 server_handler.py

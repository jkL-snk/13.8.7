FROM ubuntu:latest

RUN apt update && apt install -y wget

ENTRYPOINT wget "${1}/favicon.ico"


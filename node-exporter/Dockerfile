FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y wget tar && \
    wget https://github.com/prometheus/node_exporter/releases/download/v1.8.0/node_exporter-1.8.0.linux-amd64.tar.gz && \
    tar -xvf node_exporter-1.8.0.linux-amd64.tar.gz --strip-components=1 && \
    rm -rf node_exporter-*.tar.gz

EXPOSE 9100
CMD ["./node_exporter"]


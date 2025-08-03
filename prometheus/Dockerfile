FROM ubuntu:20.04
WORKDIR /opt/prometheus

RUN apt-get update && \
    apt-get install -y wget tar && \
    wget https://github.com/prometheus/prometheus/releases/download/v2.52.0/prometheus-2.52.0.linux-amd64.tar.gz && \
    tar -xvf prometheus-2.52.0.linux-amd64.tar.gz --strip-components=1 && \
    rm -rf prometheus-2.52.0.linux-amd64.tar.gz

COPY prometheus.yml /opt/prometheus/prometheus.yml
EXPOSE 9090
CMD ["./prometheus", "--config.file=prometheus.yml"]


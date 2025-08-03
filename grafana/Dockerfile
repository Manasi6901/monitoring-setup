FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y wget adduser libfontconfig1 && \
    wget https://dl.grafana.com/oss/release/grafana_10.4.0_amd64.deb && \
    dpkg -i grafana_10.4.0_amd64.deb && \
    rm grafana_10.4.0_amd64.deb

COPY provisioning /etc/grafana/provisioning

EXPOSE 3000
CMD ["grafana-server", "-homepath", "/usr/share/grafana"]


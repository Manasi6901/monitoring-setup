# 🛠️ Dockerized Monitoring Setup with Prometheus, Grafana, and Ansible

This project demonstrates how to **monitor a Dockerized Microservice Application** using **Prometheus**, **Node Exporter**, and **Grafana**, all installed and orchestrated via **Ansible** — without using any DockerHub images.

---

## 📌 Features

- ✅ Dockerized Prometheus, Node Exporter, Grafana — built from scratch (no DockerHub)
- ✅ Flask microservice exposing custom Prometheus metrics
- ✅ Ansible automation to:
  - Install Docker
  - Build Docker images locally
  - Deploy containers on remote Linux host
- ✅ Pre-configured Grafana dashboard with Prometheus as a data source

---

---

## 🚀 How to Use

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/Manasi6901/monitoring-setup.git
cd monitoring-setup
2️⃣ Configure Inventory
Edit ansible/inventory:

ini
Copy code
[monitoring]
<your_server_ip> ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/id_rsa
3️⃣ Run Ansible Playbooks
bash
Copy code
# Install Docker
ansible-playbook -i ansible/inventory ansible/install-docker.yml

# Build Docker images
ansible-playbook -i ansible/inventory ansible/build-prometheus.yml
ansible-playbook -i ansible/inventory ansible/build-nodeexporter.yml
ansible-playbook -i ansible/inventory ansible/build-grafana.yml

# Deploy containers
ansible-playbook -i ansible/inventory ansible/deploy-monitoring.yml
📊 Access Dashboards
Grafana: http://<your_server_ip>:3000
Login: admin / admin (default)
Add Prometheus as a data source: http://prometheus:9090

Prometheus: http://<your_server_ip>:9090

Node Exporter: http://<your_server_ip>:9100/metrics

Flask App: 


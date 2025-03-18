# Smart-Server-Monitoring
The project provides a server monitoring solution with Prometheus and a Python-based exporter which collects system metrics like CPU, Memory, Disk Usage and exposes them for Prometheus to scrape.

## Features
- Monitors CPU, Memory, and Disk usage
- Exposes metrics via HTTP
- Stores data in Prometheus
- Dockerized for easy deployment

## Steps to Run

1. Clone the Repository

```sh
git clone https://github.com/Sravankumar999/smart-server-monitoring
cd smart-server-monitoring
```

2. Build and Start the Containers

```sh
docker-compose up --build -d
```
3. Access the Services

    - Prometheus: http://localhost:9090

    - Grafana: http://localhost:3000 (Default login: admin / admin)

    - Python Exporter: http://localhost:8000/metrics

4. Configure Grafana Dashboard

    - Go to Configuration -> Data Sources -> Add Data Source

    - Select Prometheus and set URL to http://prometheus:9090

## Stopping the Services

To stop the running containers:

```sh
docker-compose down
```
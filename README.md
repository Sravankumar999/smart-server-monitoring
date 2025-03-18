# Smart-Server-Monitoring <img src="https://thumbs.dreamstime.com/z/cloud-server-line-icon-vector-simple-minimal-pictogram-web-graphics-apps-107799750.jpg" width="20" height="20"/>
The project provides a server monitoring solution with Prometheus and a Python-based exporter which collects system metrics like CPU, Memory, Disk Usage and exposes them for Prometheus to scrape.

## Features
- Monitors CPU, Memory, and Disk usage
- Exposes metrics via HTTP
- Stores data in Prometheus
- Dockerized for easy deployment

## Steps to Run
## Clone the Repository or Download via SFTP

### Option 1: Clone Using SSH
To clone the repository using SSH, follow these steps:

1. Ensure that your server is set up with SSH access.
2. Clone the repository with the following command:
   ```sh
   git clone git@github.com:Sravankumar999/smart-server-monitoring.git
   ```
3. Navigate to the project directory:
   ```sh
   cd smart-server-monitoring
   ```
### Option 2: Download and Transfer via SFTP

If you prefer to download the repository and transfer it to the server using SFTP, follow these steps:

1. Download the repository as a ZIP file from this link.

2. Use an SFTP client like scp or an SFTP GUI tool to transfer the file to your server.

    Example using scp:
   ```sh
   scp /path/to/smart-server-monitoring.zip user@server:/path/to/destination
   ```
3. SSH into your server:
```
ssh user@server
```

4. Extract the ZIP file:
```
unzip smart-server-monitoring.zip
cd smart-server-monitoring
```


<br>
After you are inside the smart-server-monitoring directory, follow the following steps:
<br><br>
Build and Start the Containers

```sh
docker-compose up --build -d
```

Access the Services

    - Prometheus: http://[SERVER_URL]:9090

    - Grafana: http://[SERVER_URL]:3000 (Default login: admin / admin)

    - Python Exporter: http://[SERVER_URL]:8000/metrics

Configure Grafana Dashboard

    - Go to Configuration -> Data Sources -> Add Data Source

    - Select Prometheus and set URL to http://prometheus:9090

## Stopping the Services

To stop the running containers:

```sh
docker-compose down
```


## TODO

- [ ] Set up alerting rules in Prometheus.
- [ ] Configure Docker Compose to scale Prometheus instances.
- [ ] Add persistent storage for Prometheus data.
- [ ] Implement authentication for Prometheus web interface.

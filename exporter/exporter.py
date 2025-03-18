import psutil
import time
from prometheus_client import start_http_server, Gauge

# Prometheus metrics definition
CPU_USAGE = Gauge('cpu_usage', 'CPU Usage')
MEMORY_USAGE = Gauge('memory_usage', 'Memory Usage')
DISK_USAGE = Gauge('disk_usage', 'Disk Usage')

# Function to collect system metrics
def collect_metrics():
    CPU_USAGE.set(psutil.cpu_percent())
    MEMORY_USAGE.set(psutil.virtual_memory().percent)
    DISK_USAGE.set(psutil.disk_usage('/').percent)

if __name__ == "__main__":
    start_http_server(8000)  # Start Prometheus HTTP server on port 8000
    print("Prometheus exporter running on port 8000...")
    while True:
        collect_metrics()
        time.sleep(5)  # Collect metrics every 5 seconds


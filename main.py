from prometheus_client import start_http_server, Gauge
import psutil
import time, os
from dotenv import load_dotenv

# Определение метрик
cpu_usage = Gauge('cpu_usage', 'Usage of CPU cores')
memory_total = Gauge('memory_total', 'Total system memory')
memory_used = Gauge('memory_used', 'Used system memory')
disk_total = Gauge('disk_total', 'Total disk space')
disk_used = Gauge('disk_used', 'Used disk space')


def collect_metrics():
    # CPU
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_usage.set(cpu_percent)

    # Memory
    memory_info = psutil.virtual_memory()
    memory_total.set(memory_info.total)
    memory_used.set(memory_info.used)

    # Disk
    disk_info = psutil.disk_usage('/')
    disk_total.set(disk_info.total)
    disk_used.set(disk_info.used)


if __name__ == "__main__":

    load_dotenv()
    host = os.getenv('EXPORTER_HOST', '0.0.0.0')
    port = int(os.getenv('EXPORTER_PORT', '8000'))

    start_http_server(port, addr=host)
    print(f"Exporter running on port:{port}")

    while True:
        collect_metrics()
        time.sleep(5)

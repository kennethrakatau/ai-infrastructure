import os
import platform
from datetime import datetime

region = os.getenv("REGION", "unknown")

log_file = "/app/logs/system_metrics.log"

metrics = (
    f"Time: {datetime.now()}\n"
    f"OS Kernel: {platform.system()}\n"
    f"CPU Cores: {os.cpu_count()}\n"
    f"Deployment Region: {region}\n"
    f"{'-' * 40}\n"
)

os.makedirs("/app/logs", exist_ok=True)
with open(log_file, "a") as file:
    file.write(metrics)

print(metrics)
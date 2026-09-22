import os
import platform

region = os.getenv("REGION", "unknown")

print(f"OS Kernel: {platform.system()}")
print(f"CPU Cores: {os.cpu_count()}")
print(f"Deployment Region: {region}")
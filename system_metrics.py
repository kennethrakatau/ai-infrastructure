import os
import platform

print(f"OS Kernel: {platform.system()}")
print(f"CPU Cores: {os.cpu_count()}")
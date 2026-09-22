FROM python:3.10-slim
COPY system_metrics.py /app/system_metrics.py
CMD ["python3", "/app/system_metrics.py"]

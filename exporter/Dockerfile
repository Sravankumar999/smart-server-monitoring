FROM python:3.9-slim

WORKDIR /app

COPY exporter.py /app/

RUN pip install prometheus_client psutil

EXPOSE 8000

CMD ["python", "exporter.py"]

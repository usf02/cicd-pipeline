FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

EXPOSE 8000

ENV ENVIRONMENT=local
ENV VERSION=1.0.0

CMD ["python", "main.py"]

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY agents_demo.py /app/agents_demo.py

RUN pip install --no-cache-dir \
    aiokafka \
    openai \
    langchain-openai

ENV KAFKA_BOOTSTRAP_SERVERS=broker:9092 \
    OPENAI_MODEL=gpt-4o-mini

CMD ["python", "agents_demo.py"]

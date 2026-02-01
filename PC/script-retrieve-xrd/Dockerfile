FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    cmake \
    g++ \
    gcc \
    libssl-dev \
    libxml2-dev \
    uuid-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "script.py"]

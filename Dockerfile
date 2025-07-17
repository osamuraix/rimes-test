# syntax=docker/dockerfile:1
FROM python:3.11-slim

# Environment config
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project code
COPY . .

# Copy scripts and give permission
COPY entrypoint.sh wait-for-postgres.sh create_superuser.py ./
RUN chmod +x /app/entrypoint.sh /app/wait-for-postgres.sh

# Expose port for Gunicorn
EXPOSE 8000

# Default command
ENTRYPOINT ["/app/entrypoint.sh"]
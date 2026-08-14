FROM python:3.13-slim

# Set environment variables
ENV DATABASE_NAME="book_store"
ENV DATABASE_HOST="postgres:password@book_store_db"
ENV PYTHONUNBUFFERED=1

# Copy and install dependencies with cache cleanup
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Copy application code
COPY . .

CMD ["python", "app.py"]
FROM python:3.13-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:3.13-slim

ENV DATABASE_NAME="book_store"
ENV DATABASE_HOST="postgres:password@book_store_db"
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy only the installed packages from builder
COPY --from=builder /root/.local /root/.local

# Copy application code
COPY . .

ENV PATH=/root/.local/bin:$PATH

CMD ["python", "app.py"]
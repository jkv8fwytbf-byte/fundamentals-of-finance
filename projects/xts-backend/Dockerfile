FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Wait for Postgres, run migrations, then start uvicorn (see entrypoint.sh).
# Invoked via "sh" so it works regardless of the file's executable bit.
CMD ["sh", "/app/entrypoint.sh"]

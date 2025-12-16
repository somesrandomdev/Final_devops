# Stage 1: Build dependencies
FROM python:3.12-slim AS builder
WORKDIR /app

# <-- ADD THIS BACK
COPY requirements.txt .

RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Final lightweight image
FROM python:3.12-slim

RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder --chown=appuser:appgroup /root/.local /home/appuser/.local

# Copy app code
COPY --chown=appuser:appgroup app ./app

USER appuser

ENV PATH=/home/appuser/.local/bin:$PATH

ARG GIT_HASH=unknown
ENV GIT_HASH=$GIT_HASH

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# Stage 1: Build dependencies
FROM python:3.12-slim AS builder
WORKDIR /app

# Install build dependencies if needed (usually not for pure Python)
# COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Final lightweight image
FROM python:3.12-slim

# Create non-root user for security (best practice in prod)
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder --chown=appuser:appgroup /root/.local /home/appuser/.local

# Copy app code
COPY --chown=appuser:appgroup app ./app

# Switch to non-root user
USER appuser

# Make installed bins available
ENV PATH=/home/appuser/.local/bin:$PATH

# Inject Git hash at build time (great for debugging!)
ARG GIT_HASH=unknown
ENV GIT_HASH=$GIT_HASH

# Expose correct port
EXPOSE 8000

# Run Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
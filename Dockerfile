# Stage 1: Build dependencies
FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Final lightweight image
FROM python:3.12-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local

# Copy le contenu du dossier app/ directement à la racine de /app
COPY app/ .

# Ajouter les binaires installés par l'utilisateur au PATH
ENV PATH=/root/.local/bin:$PATH

# Injection du GIT_HASH au moment du build (default: unknown)
ARG GIT_HASH=unknown
ENV GIT_HASH=$GIT_HASH

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
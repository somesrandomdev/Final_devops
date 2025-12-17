import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse  # Better import (from fastapi.responses)

app = FastAPI(title="Mon appli – Personne 2")

# Fallback to "unknown" if env var missing, limit to 7 chars
GIT_HASH = os.getenv("GIT_HASH", "unknown")[:7]

@app.get("/")
async def root():
    return {
        "message": "Hello le prof, tout marche ! CI/CD fully working 🚀",
        "git_hash": os.getenv("GIT_HASH", "unknown")
    }

@app.get("/health")
async def health():
    return {"status": "healthy", "git_hash": os.getenv("GIT_HASH", "unknown")}
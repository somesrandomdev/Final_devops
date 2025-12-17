import os
from fastapi import FastAPI

app = FastAPI(title="Mon appli – Personne 2")

# Hash court (7 premiers caractères) ou "unknown"
GIT_HASH_SHORT = os.getenv("GIT_HASH", "unknown")[:7]

@app.get("/")
async def root():
    full_hash = os.getenv("GIT_HASH", "unknown")
    return {
        "message": "Hello le prof, tout marche ! CI/CD fully working 🚀",
        "git_hash": GIT_HASH_SHORT,
        "full_git_hash": full_hash
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "git_hash": GIT_HASH_SHORT
    }

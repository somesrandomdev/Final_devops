import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse  # Better import (from fastapi.responses)

app = FastAPI(title="Mon appli – Personne 2")

# Fallback to "unknown" if env var missing, limit to 7 chars
GIT_HASH = os.getenv("GIT_HASH", "unknown")[:7]

@app.get("/")
async def root():
    return {
        "message": "Hello le prof, tout marche !",
        "version": "1.0.0",
        "commit": GIT_HASH
    }

@app.get("/health")
async def health():
    # Simpler: FastAPI auto-sets 200 for dict return
    return {"status": "OK"}
    # Or keep JSONResponse if you prefer explicit control
    # return JSONResponse(status_code=200, content={"status": "OK"})
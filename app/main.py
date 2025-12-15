import os
from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI(title="Mon appli – Personne 2")

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
    return JSONResponse(status_code=200, content={"status": "OK"})
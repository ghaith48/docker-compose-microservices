from fastapi import FastAPI
import os

app = FastAPI(title="DevOps Microservice API")

@app.get("/")
def root():
    return {
        "service": "backend",
        "status": "running",
        "environment": os.getenv("ENV", "local")
    }

@app.get("/health")
def health():
    return {"status": "healthy"}


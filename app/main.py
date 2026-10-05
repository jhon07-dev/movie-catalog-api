from fastapi import FastAPI

from app.database.connection import client

app = FastAPI()


@app.get("/health")
def health_check():
    try:
        client.admin.command("ping")
        return {
            "api": "ok",
            "database": "connected"
        }
    except Exception:
        return {
            "api": "ok",
            "database": "disconnected"
        }
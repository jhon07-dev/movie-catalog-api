from fastapi import FastAPI

app = FastAPI(
    title="Movie Catalog API",
    description="REST API for managing movies",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Movie Catalog API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
from fastapi import FastAPI

app = FastAPI(title="Smart Waste Sorting Robot")


@app.get("/ping")
def ping():
    """Health check endpoint."""
    return {"status": "ok"}
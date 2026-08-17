from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Skylo API")


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {
        "name": "Skylo",
        "status": "online",
        "message": "Skylo backend is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "skylo-api"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "message": request.message,
        "response": "Skylo received your message."
    }
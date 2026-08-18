from fastapi import FastAPI
from pydantic import BaseModel

from app.llm.base import LLMMessage
from app.llm.nemotron import NemotronProvider


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
async def chat(request: ChatRequest):
    provider = NemotronProvider()

    response = await provider.generate(
        [
            LLMMessage(
                role="user",
                content=request.message
            )
        ]
    )

    return {
        "message": request.message,
        "response": response.content,
        "model": response.model
    }
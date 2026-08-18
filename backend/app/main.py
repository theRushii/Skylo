from fastapi import FastAPI
from pydantic import BaseModel

from app.conversation.manager import ConversationManager
from app.llm.nemotron import NemotronProvider


app = FastAPI(title="Skylo API")

conversation = ConversationManager()
provider = NemotronProvider()


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
    conversation.add_user_message(request.message)

    response = await provider.generate(
        conversation.get_messages()
    )

    conversation.add_assistant_message(
        response.content
    )

    return {
        "message": request.message,
        "response": response.content,
        "model": response.model
    }


@app.delete("/chat")
def clear_chat():
    conversation.clear()

    return {
        "status": "cleared"
    }
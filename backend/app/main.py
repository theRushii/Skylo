from collections.abc import AsyncIterator

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from app.conversation.manager import ConversationManager
from app.llm.nemotron import NemotronProvider


app = FastAPI(title="Skylo API")

conversation = ConversationManager()
provider = NemotronProvider()


class ChatRequest(BaseModel):
    conversation_id: str
    message: str


@app.get("/")
def root():
    return {
        "name": "Skylo",
        "status": "online",
        "message": "Skylo backend is running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "skylo-api",
    }


@app.post("/chat")
async def chat(request: ChatRequest):
    conversation.add_user_message(
        request.conversation_id,
        request.message,
    )

    response = await provider.generate(
        conversation.get_messages(request.conversation_id)
    )

    conversation.add_assistant_message(
        request.conversation_id,
        response.content,
    )

    return {
        "conversation_id": request.conversation_id,
        "message": request.message,
        "response": response.content,
        "model": response.model,
    }


@app.post("/chat/stream")
async def chat_stream(request: ChatRequest):
    conversation.add_user_message(
        request.conversation_id,
        request.message,
    )

    async def stream_response() -> AsyncIterator[str]:
        full_response = ""

        async for chunk in provider.stream(
            conversation.get_messages(request.conversation_id)
        ):
            full_response += chunk
            yield chunk

        conversation.add_assistant_message(
            request.conversation_id,
            full_response,
        )

    return StreamingResponse(
        stream_response(),
        media_type="text/plain",
    )


@app.delete("/chat/{conversation_id}")
def clear_chat(conversation_id: str):
    conversation.clear(conversation_id)

    return {
        "conversation_id": conversation_id,
        "status": "cleared",
    }
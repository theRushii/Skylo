from app.llm.base import LLMMessage


class ConversationManager:
    """
    Stores conversation messages for the current Skylo session.
    """

    def __init__(self) -> None:
        self.messages: list[LLMMessage] = []

    def add_user_message(self, content: str) -> None:
        self.messages.append(
            LLMMessage(
                role="user",
                content=content,
            )
        )

    def add_assistant_message(self, content: str) -> None:
        self.messages.append(
            LLMMessage(
                role="assistant",
                content=content,
            )
        )

    def get_messages(self) -> list[LLMMessage]:
        return self.messages.copy()

    def clear(self) -> None:
        self.messages.clear()
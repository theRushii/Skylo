from app.llm.base import LLMMessage


class ConversationManager:
    """
    Stores multiple Skylo conversations in memory.
    """

    def __init__(self) -> None:
        self.conversations: dict[str, list[LLMMessage]] = {}

    def create_conversation(self, conversation_id: str) -> None:
        if conversation_id not in self.conversations:
            self.conversations[conversation_id] = []

    def add_user_message(
        self,
        conversation_id: str,
        content: str,
    ) -> None:
        self.create_conversation(conversation_id)

        self.conversations[conversation_id].append(
            LLMMessage(
                role="user",
                content=content,
            )
        )

    def add_assistant_message(
        self,
        conversation_id: str,
        content: str,
    ) -> None:
        self.create_conversation(conversation_id)

        self.conversations[conversation_id].append(
            LLMMessage(
                role="assistant",
                content=content,
            )
        )

    def get_messages(
        self,
        conversation_id: str,
    ) -> list[LLMMessage]:
        self.create_conversation(conversation_id)

        return self.conversations[conversation_id].copy()

    def clear(
        self,
        conversation_id: str,
    ) -> None:
        self.conversations.pop(conversation_id, None)
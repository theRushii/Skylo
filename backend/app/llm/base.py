from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class LLMMessage:
    role: str
    content: str


@dataclass
class LLMResponse:
    content: str
    model: str


class LLMProvider(ABC):
    """
    Base interface that every Skylo LLM provider must implement.
    """

    @abstractmethod
    async def generate(
        self,
        messages: list[LLMMessage],
    ) -> LLMResponse:
        """
        Generate a response from the language model.
        """
        raise NotImplementedError
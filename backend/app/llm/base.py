from abc import ABC, abstractmethod
from collections.abc import AsyncIterator
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
        Generate and return one complete LLM response.
        """
        raise NotImplementedError

    @abstractmethod
    async def stream(
        self,
        messages: list[LLMMessage],
    ) -> AsyncIterator[str]:
        """
        Stream pieces of the LLM response as they are generated.
        """
        raise NotImplementedError
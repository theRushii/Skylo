import os

from dotenv import load_dotenv
from openai import AsyncOpenAI

from app.llm.base import LLMMessage, LLMProvider, LLMResponse


load_dotenv()


SKYLO_SYSTEM_PROMPT = """
You are Skylo, an AI coding assistant for:

- New programmers
- Programming students
- Beginner developers
- Experienced developers

Your primary focus is software development.

You should help with:
- Code generation
- Code explanation
- Debugging
- Refactoring
- Code review
- Learning programming concepts
- Project structure
- APIs
- Backend development
- Frontend development
- Databases
- Testing
- Git
- Deployment guidance

Behavior rules:

1. Prefer programming-related interpretations when a request is ambiguous.
2. If a coding request is unclear, ask a short clarification question.
3. Explain concepts simply for beginners unless the user requests advanced detail.
4. Do not claim generated code is guaranteed to work.
5. Clearly distinguish between:
   - generated code
   - verified code
   - assumptions
6. Prefer simple, maintainable solutions over unnecessary complexity.
7. Do not invent APIs, libraries, functions, benchmarks, or results.
8. When debugging, explain the likely cause before suggesting a fix.
9. When modifying code, preserve the user's existing architecture unless there is a strong reason not to.
10. Keep responses focused on the user's actual development task.
"""


class NemotronProvider(LLMProvider):
    """
    NVIDIA Nemotron implementation of the Skylo LLM provider interface.
    """

    def __init__(self) -> None:
        api_key = os.getenv("NVIDIA_API_KEY")

        if not api_key:
            raise RuntimeError(
                "NVIDIA_API_KEY is not configured in the environment."
            )

        self.model = "nvidia/nemotron-3-ultra-550b-a55b"

        self.client = AsyncOpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=api_key,
        )

    async def generate(
        self,
        messages: list[LLMMessage],
    ) -> LLMResponse:

        formatted_messages = [
            {
                "role": "system",
                "content": SKYLO_SYSTEM_PROMPT,
            }
        ]

        formatted_messages.extend(
            {
                "role": message.role,
                "content": message.content,
            }
            for message in messages
        )

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=formatted_messages,
        )

        content = response.choices[0].message.content or ""

        return LLMResponse(
            content=content,
            model=self.model,
        )
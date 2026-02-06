from openai import AsyncOpenAI

from app.config import settings
from app.prompt import SYSTEM_PROMPT, build_user_prompt


class LLMService:
    def __init__(self) -> None:
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)

    async def explain_code(self, code: str, language: str) -> str:
        response = await self.client.chat.completions.create(
            model=settings.openai_model,
            temperature=0.2,
            timeout=settings.openai_timeout_seconds,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": build_user_prompt(code, language)},
            ],
        )
        content = response.choices[0].message.content
        return content.strip() if content else "Не удалось получить объяснение."

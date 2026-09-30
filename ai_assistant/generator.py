from openai import OpenAI

from config.settings import settings

from ai_assistant.prompts import (
    TEST_GENERATION_PROMPT
)


class AITestGenerator:

    def __init__(self):

        if not settings.OPENAI_API_KEY:

            raise ValueError(
                "OPENAI_API_KEY is not configured."
            )

        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    def generate_tests(
        self,
        requirement: str
    ):

        response = self.client.responses.create(

            model=settings.OPENAI_MODEL,

            instructions=(
                TEST_GENERATION_PROMPT
            ),

            input=requirement
        )

        return response.output_text
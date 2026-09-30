from openai import OpenAI

from config.settings import settings

from ai_assistant.prompts import (
    FAILURE_ANALYSIS_PROMPT
)


class AITestAnalyzer:

    def __init__(self):

        if not settings.OPENAI_API_KEY:

            raise ValueError(
                "OPENAI_API_KEY is not configured."
            )

        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    def analyze_failure(
        self,
        test_name: str,
        error_message: str,
        logs: str
    ):

        input_text = f"""
Test name:
{test_name}

Error:
{error_message}

Logs:
{logs}
"""

        response = self.client.responses.create(

            model=settings.OPENAI_MODEL,

            instructions=(
                FAILURE_ANALYSIS_PROMPT
            ),

            input=input_text
        )

        return response.output_text
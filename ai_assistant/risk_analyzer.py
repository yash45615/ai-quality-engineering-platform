from openai import OpenAI

from config.settings import settings

from ai_assistant.prompts import (
    RISK_ANALYSIS_PROMPT
)


class RiskAnalyzer:

    def __init__(self):

        if not settings.OPENAI_API_KEY:

            raise ValueError(
                "OPENAI_API_KEY is not configured."
            )

        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    def analyze_change(
        self,
        changed_files: str
    ):

        response = self.client.responses.create(

            model=settings.OPENAI_MODEL,

            instructions=(
                RISK_ANALYSIS_PROMPT
            ),

            input=changed_files
        )

        return response.output_text
from app.core.gemini_client import client
from app.core.langchain_llm import googleLLM
from app.prompt_templates.classifier_prompt_template import (classifier_prompt)

import json


class ClassifierAgent:
    def run(self, issue: str):

        prompt = classifier_prompt.format(issue=issue)

        response = googleLLM.invoke(prompt)

        cleanedResponse = (
            response.content.replace("```json", "").replace("```", "").strip()
        )

        return json.loads(cleanedResponse)


classifier_agent = ClassifierAgent()

from app.core.gemini_client import client
from app.core.langchain_llm import googleLLM
from app.prompt_templates.severity_prompt_template import (severity_prompt)
import json


class SeverityAgent:

    def run(
        self,
        issue: str,
        module: str,
        issue_type: str
    ):

        prompt = severity_prompt.format(issue=issue,module=module,issue_type=issue_type)

        response = googleLLM.invoke(prompt)

        cleaned = (
            response.content.replace("```json", "").replace("```", "").strip()
        )
        return json.loads(cleaned)


severity_agent = SeverityAgent()

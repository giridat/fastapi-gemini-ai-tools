from app.core.gemini_client import client
from app.core.langchain_llm import googleLLM
from app.prompt_templates.jira_prompt_template import (jira_prompt)
import json


class JiraAgent:

    def run(self, issue: str, severity: str):

        prompt = jira_prompt.format(issue=issue, severity=severity)
        response = googleLLM.invoke(prompt)

        cleanedResponse = (
            response.content.replace("```json", "").replace("```", "").strip()
        )

        return json.loads(cleanedResponse)


jira_agent = JiraAgent()

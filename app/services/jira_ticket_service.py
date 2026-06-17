from app.core.gemini_client import client
import json


class JiraTicketSerivce:

    def generate_ticket(
        self,
        issue: str
    ):

        prompt = f"""
        You are a Senior QA Lead.

        Generate a Jira ticket.

        Return ONLY valid JSON.

        Schema:

        {{
            "title": "",
            "description": "",
            "severity": "",
            "priority": "",
            "labels": []
        }}

        Severity values:
        - Critical
        - High
        - Medium
        - Low

        Priority values:
        - P1
        - P2
        - P3
        - P4

        Issue:

        {issue}
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        cleaned_response = (
            response.text.replace("```json", "").replace("```", "").strip()
        )

        return json.loads(cleaned_response)


jira_ticket_service = JiraTicketSerivce()

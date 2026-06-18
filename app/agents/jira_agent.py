from app.core.gemini_client import client
import json


class JiraAgent:

    def run(self, issue: str, severity: str):

        prompt = f"""
        Create Jira Ticket.

        Issue:
        {issue}

        Severity:
        {severity}

        Return JSON:

        {{
            "title":"",
            "description":"",
            "labels":[]
        }}
        
         """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        cleanedResponse = (
            response.text.replace("```json", "").replace("```", "").strip()
        )

        return json.loads(cleanedResponse)


jira_agent = JiraAgent()

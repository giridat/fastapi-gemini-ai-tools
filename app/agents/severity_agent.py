from app.core.gemini_client import client
import json


class SeverityAgent:

    def run(
        self,
        issue: str,
        module: str,
        issue_type: str
    ):

        prompt = f""" 
        Determine severity.

        Issue:
        {issue}

        Module:
        {module}

        Issue Type:
        {issue_type}

        Return JSON:

        {{
            "severity":"",
            "priority":""
        }}
        
        
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        cleaned = (
            response.text.replace("```json", "").replace("```", "").strip()
        )
        return json.loads(cleaned)


severity_agent = SeverityAgent()

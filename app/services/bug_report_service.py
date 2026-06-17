from app.core.gemini_client import client
import json


class BugReportService:

    def generate_report(
        self,
        issue: str
    ):

        prompt = f"""
        You are a Senior QA Engineer.

        Analyze the issue and return ONLY valid JSON.

        Schema:

        {{
            "summary": "",
            "severity": "",
            "priority": "",
            "root_cause": "",
            "steps_to_reproduce": []
        }}

        Issue:

        {issue}

        Return JSON only.
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        cleaned_response = (
            response.text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        try:
            result = json.loads(cleaned_response)

            return result
        except json.JSONDecodeError:
            return{
                 "summary": "Unable to parse AI response",
                 "severity": "Unknown",
                 "priority": "P4",
                 "root_cause": cleaned_response,
                "steps_to_reproduce": []
            }

bug_report_service = BugReportService()
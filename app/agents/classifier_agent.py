from app.core.gemini_client import client
import json

class ClassifierAgent:
    def run(self,issue:str):

        prompt = f""""
        Classify the bug. 

        Issue:
        {issue}

        Return JSON:

        {{
            "module":"",
            "issue_type":""
        }}
        """

        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents=prompt
        )

        cleanedResponse = (
            response.text.replace("```json","").replace("```","").strip()
        )

        return json.loads(cleanedResponse)



classifer_agent = ClassifierAgent()        
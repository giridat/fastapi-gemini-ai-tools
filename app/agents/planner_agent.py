from app.core.gemini_client import client
from app.core.langchain_llm import googleLLM
from app.prompt_templates.planner_template import(planner_template)
import json

class PlannerAgent:
    def run(self,issue:str):
        prompt = planner_template.format(issue=issue)

        response = googleLLM.invoke(prompt)

        cleanedResponse = (
            response.content.replace("```json","").replace("```","").strip()    
        )

        return json.loads(cleanedResponse)
planner_agent = PlannerAgent()
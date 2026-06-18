from app.core.langchain_llm import googleLLM
from langchain_core.prompts import PromptTemplate

jira_prompt = PromptTemplate.from_template(""" 
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

""")

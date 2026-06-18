from app.core.langchain_llm import googleLLM
from langchain_core.prompts import PromptTemplate

severity_prompt = PromptTemplate.from_template(
    """
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
)

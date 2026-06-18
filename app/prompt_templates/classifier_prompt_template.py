from app.core.langchain_llm import googleLLM
from langchain_core.prompts import PromptTemplate
import json

classifier_prompt = PromptTemplate.from_template(
    """
    Clasify the bug.

    Issue:
    {issue}

    Return ONLY valid JSON.

    Schema:

    {{
        "module":"",
        "issue_type":""
    }}
    
    """
)
from app.core.langchain_llm import googleLLM
from langchain_core.prompts import PromptTemplate

planner_template = PromptTemplate.from_template(""" 
You are a workflow planner.

Analyze the request and determine which agents should run.

Available agents:

1. Classification Agent
2. Severity Agent
3. Jira Agent

Return ONLY JSON.

Schema:

{{
    "run_classification": true,
    "run_severity": true,
    "run_jira": true
}}

Request:

{issue}


""")

from pydantic import BaseModel


class AgentWorkflowRequest(BaseModel):
    issue:str


class AgentWorkflowResponse(BaseModel):
    classification:dict
    severity:dict
    jira_ticket:dict
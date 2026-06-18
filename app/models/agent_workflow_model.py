from pydantic import BaseModel
from typing import Optional


class AgentWorkflowRequest(BaseModel):
    issue: str


class AgentWorkflowResponse(BaseModel):
    issue: Optional[str] = None
    plan: Optional[dict] = None
    classification: Optional[dict] = None
    severity: Optional[dict] = None
    jira_ticket: Optional[dict] = None
    error: Optional[str] = None

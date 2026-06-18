from fastapi import APIRouter

from app.models.agent_workflow_model import (
    AgentWorkflowRequest,
    AgentWorkflowResponse
)

from app.workflows.bug_workflow import (
    bug_workflow
)

router = APIRouter(
    prefix="/agentic-bug",
    tags=["Agentic AI"]
)


@router.post("/", response_model=AgentWorkflowResponse)
def analyze_bug(request: AgentWorkflowRequest):
    return bug_workflow.run(request.issue)

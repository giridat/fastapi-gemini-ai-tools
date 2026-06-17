from fastapi import APIRouter

from app.models.jira_ticket_model import (
    JiraTicketRequest,
    JiraTicketResponse
)

from app.services.jira_ticket_service import (
    jira_ticket_service
)


router = APIRouter(
    prefix="/jira-ticket",
    tags=["Jira Ticket"]
)


@router.post(
    "/",
    response_model=JiraTicketResponse
)
def generate_jira_ticket(
    request: JiraTicketRequest
):
    return jira_ticket_service.generate_ticket(request.issue)

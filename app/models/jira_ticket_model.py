from pydantic import BaseModel

class JiraTicketRequest(BaseModel):
    issue:str


class JiraTicketResponse(BaseModel):
    title:str
    description:str
    severity: str
    priority:str
    labels: list[str]
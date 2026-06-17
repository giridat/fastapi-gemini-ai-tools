from pydantic import BaseModel


class BugReportRequest(BaseModel):
    issue: str


class BugReportResponse(BaseModel):
    summary: str
    severity: str
    priority: str
    root_cause: str
    steps_to_reproduce: list[str]
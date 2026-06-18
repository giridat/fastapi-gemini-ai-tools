from fastapi import APIRouter

from app.models.bug_report_model import (
    BugReportRequest,
    BugReportResponse
)

from app.services.bug_report_service import (
    bug_report_service
    
)

router = APIRouter(
    prefix="/bug-report",
    tags=["Bug Report"]
)

@router.post(
    "/",
    response_model=BugReportResponse
)


def generate_bug_report(
    request: BugReportRequest
):

    report = bug_report_service.generate_report(
        request.issue
    )

    print(report)

    return {
        "report":report
    }

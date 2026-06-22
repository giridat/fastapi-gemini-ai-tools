
from fastapi import FastAPI
from app.routes.flutter_review_route import (
    router as flutter_review_router
)
from app.routes.bug_report_route import (
    router as bug_report_router
)

from app.routes.jira_ticket_route import (
    router as jira_ticket_router
)

from app.routes.agentic_bug_route import (
    router as agentic_bug_router
)

from app.routes.bug_route import router as bug_router

app = FastAPI(
    title="AI Career Assistance"
)


app.include_router(
    flutter_review_router
)

app.include_router(
    bug_report_router
)

app.include_router(
    jira_ticket_router

)


app.include_router(
    agentic_bug_router
)
app.include_router(
    bug_router
)


@app.get("/")
def home():

    return {
        "message": "Assiant is running"
    }

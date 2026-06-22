from fastapi import APIRouter

from app.models.bug_create_request import (BugCreateRequestModel)
from app.models.bug_update_request import (BugUpdateRequestModel)

from app.services.bug_service import (bug_service)

router = APIRouter()


@router.post("/create-bug")
def create_bug(request: BugCreateRequestModel):
    return bug_service.create_bug(request)

@router.put("/update-bugs/{bug_id}")
def update_bug(
    bug_id: str,
    request: BugUpdateRequestModel
):

    return bug_service.update_bug(
        bug_id,
        request
    )  


@router.get("/bugs")
def get_all_bugs():
    return bug_service.get_all_bugs()


@router.get("/bugs/{bug_id}")
def get_bug(
    bug_id: str
):
    return bug_service.get_bug_by_id(bug_id)

@router.delete("/bugs/{bug_id}")
def delete_bug(bug_id:str):
    return {
        "deleted":
        bug_service.delete_bug(bug_id)
    }    

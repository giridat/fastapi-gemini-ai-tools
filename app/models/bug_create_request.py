from pydantic import BaseModel

class BugCreateRequestModel(BaseModel):
    bug_id:str
    title:str
    description:str
    root_cause:str
    fix:str
    severity:str
    module:str
    issue_type:str
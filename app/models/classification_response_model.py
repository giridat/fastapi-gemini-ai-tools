from pydantic import BaseModel

class ClassificationResponse(BaseModel):
    module:str
    issue_type:str
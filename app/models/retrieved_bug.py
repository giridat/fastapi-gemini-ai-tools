
from pydantic import BaseModel

class RetrievedBug(BaseModel):
   bug_id:str
   title:str
   description:str
   fix:str

from enum import Enum
from pydantic import field_validator

class Severity(str, Enum):
    CRITICAL = "Critical"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class Priority(str, Enum):
    P1= "P1"
    P2 =  "P2"
    P3 = "P3"
    P4 = "P4"
    
@field_validator("severity", mode="before")
@classmethod
def normailize_severity(cls,value):
    if isinstance(value,str):
        mapping =  {
            "critical":"Critical",
            "high":"High",
            "medium":"Medium",
            "low":"Low"
        }

        return mapping.get(value.lower(),value)
    return value

@field_validator("priority", mode="before")
@classmethod
def normalize_priority(cls,value):
    if isinstance(value,str):
        return value.upper()
    return value           

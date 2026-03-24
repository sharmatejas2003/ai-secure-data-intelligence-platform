from pydantic import BaseModel
from typing import List

class Finding(BaseModel):
    type: str
    risk: str
    line: int

class ResponseModel(BaseModel):
    summary: str
    findings: List[Finding]
    risk_score: int
    risk_level: str
    insights: List[str]
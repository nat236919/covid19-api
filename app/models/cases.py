
from pydantic import BaseModel

class caseBase(BaseModel):
    def case(self):
        dt: str
        ts: int
    
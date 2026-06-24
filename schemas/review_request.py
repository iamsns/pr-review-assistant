from pydantic import BaseModel

class PRRequest(BaseModel):
    pr: str
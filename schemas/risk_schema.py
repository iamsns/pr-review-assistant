from pydantic import BaseModel, Field


class RiskScoreResponse(BaseModel):
    score: int = Field(
        description="Overall pull request risk score from 0 to 10."
    )

    risk: str = Field(
        description="Overall risk level. One of: Low, Medium, High, Critical."
    )

    reason: str = Field(
        description="Short explanation summarizing the main reasons for the assigned risk."
    )
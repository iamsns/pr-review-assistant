from typing import List, Optional

from pydantic import BaseModel, model_validator

class PROverviewRequest(BaseModel):
    url: Optional[str] = None
    owner: Optional[str] = None
    repo: Optional[str] = None
    pr_number: Optional[int] = None
    authentication_token: Optional[str] = None
    
    @model_validator(mode="after")
    def validate_pr_input(self):
        has_url = bool(self.url)
        has_parts = all([
            self.owner,
            self.repo,
            self.pr_number is not None
        ])

        if not (has_url or has_parts):
            raise ValueError(
                "Either provide 'url' or provide 'owner', 'repo', and 'pr_number'."
            )

        return self

class ReviewResponse(BaseModel):
    success: bool
    message: str
    
class FileChange(BaseModel):
    file_name: str
    change_type: str
    additions: int
    deletions: int
    changes: int
    patch: str

class PROverviewData(BaseModel):
    files_changed: int
    files: List[FileChange]
    total_additions: int
    total_deletions: int
    
    
class PROverview(BaseModel):
    success: bool
    message: str
    data: PROverviewData
    
class PRSummary(BaseModel):
    summary: str
    key_changes: List[str]
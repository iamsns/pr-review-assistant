from typing import List

from pydantic import BaseModel

class ReviewResponse(BaseModel):
    success: bool
    message: str
    
class FileChange(BaseModel):
    file_name: str
    change_type: str
    additions: int
    deletions: int

class PROverviewData(BaseModel):
    files_changed: int
    files: list[FileChange]
    total_additions: int
    total_deletions: int
    
    
class PROverview(BaseModel):
    success: bool
    message: str
    data: PROverviewData
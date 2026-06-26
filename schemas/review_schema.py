from typing import Literal
from pydantic import BaseModel, Field


class BugIssue(BaseModel):
    severity: Literal["High", "Medium", "Low"] = Field(
        description="Risk level of the issue"
    )
    type: str = Field(
        description="Category of the issue"
    )
    file: str = Field(
        description="File that contains issue"
    )
    description: str = Field(
        description="Explanation of the detected issue"
    )
    suggestion: str = Field(
        description="Recommended fix"
    )


class BugReviewResponse(BaseModel):
    issues: list[BugIssue] = Field(
        default_factory=list,
        description="List of detected issues"
    )


class ReviewComment(BaseModel):
    type: str = Field(
        description="Category of the review comment such as Validation, Error Handling, Performance, Security, Maintainability, or Best Practice."
    )

    comment: str = Field(
        description="A concise review comment explaining the identified concern and why it should be addressed."
    )

    file_name: str | None = Field(
        default=None,
        description="Name of the file where the issue was detected. Null if the comment applies to the overall pull request."
    )

    line_number: int | None = Field(
        default=None,
        description="Approximate line number in the file related to the comment. Null if a specific line cannot be determined."
    )

    suggestion: str = Field(
        description="Recommended action or code change that would resolve or improve the identified issue."
    )


class ReviewCommentsResponse(BaseModel):
    comments: list[ReviewComment] = Field(
        default_factory=list,
        description="List of AI-generated review comments for the pull request. Empty if no review comments are required."
    )
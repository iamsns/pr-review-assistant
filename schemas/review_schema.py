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

class SecurityIssue(BaseModel):
    severity: str = Field(
        description="High, Medium or Low."
    )

    type: str = Field(
        description="Category of the security issue."
    )

    description: str = Field(
        description="Explanation of the security concern."
    )

    file_name: str | None = Field(
        default=None,
        description="File containing the issue."
    )

    line_number: int | None = Field(
        default=None,
        description="Changed line where the issue occurs."
    )

    vulnerable_code: str | None = Field(
        default=None,
        description="Relevant code snippet."
    )

    recommendation: str = Field(
        description="Recommended secure implementation."
    )


class SecurityReviewResponse(BaseModel):
    security_issues: list[SecurityIssue] = Field(
        default_factory=list,
        description="List of security issues."
    )
    

class PerformanceIssue(BaseModel):
    severity: str = Field(
        description="Impact level of the performance issue. One of: High, Medium, Low."
    )
    type: str = Field(
        description="Category of the performance issue (e.g. N+1 Query, Inefficient Loop, High Memory Usage, Missing Pagination, Algorithm Inefficiency)."
    )
    description: str = Field(
        description="Clear explanation of the performance issue and why it may degrade application performance."
    )
    file_name: str = Field(
        description="Relative path of the file containing the performance issue."
    )
    line_number: int | None = Field(
        default=None,
        description="Approximate line number where the issue occurs. Use null if it cannot be determined."
    )
    inefficient_code: str | None = Field(
        default=None,
        description="Relevant code snippet responsible for the performance issue. Use null if unavailable."
    )
    recommendation: str = Field(
        description="Recommended change to improve performance and eliminate the issue."
    )


class PerformanceReviewResponse(BaseModel):
    performance_issues: list[PerformanceIssue] = Field(
        description="List of performance issues found in the pull request. Return an empty list if no issues are detected."
    )
from fastapi import APIRouter, Request

from schemas.review_schema import BugReviewResponse, ReviewCommentsResponse, SecurityReviewResponse
from schemas.overview_schema import PROverviewRequest
from services.review_service import ReviewService

router = APIRouter()

review_service = ReviewService()

@router.post("/bug-review", response_model=BugReviewResponse)
def bug_review(request: PROverviewRequest):
    return review_service.get_bug_review(request)

@router.post("/comments", response_model=ReviewCommentsResponse)
def review_comment(request: PROverviewRequest):
    return review_service.get_review_comments(request)

@router.post("/security-issue", response_model=SecurityReviewResponse)
def security_review(request: PROverviewRequest):
    return review_service.get_security_review(request)
from fastapi import APIRouter, Request

from schemas.review_schema import BugReviewResponse, ReviewCommentsResponse, SecurityReviewResponse, PerformanceReviewResponse, TestCaseResponse
from schemas.overview_schema import PROverviewRequest
from schemas.risk_schema import RiskScoreResponse
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

@router.post("/performance-review", response_model=PerformanceReviewResponse)
def performance_review(request: PROverviewRequest):
    return review_service.get_performance_review(request)

@router.post("/test-case", response_model=TestCaseResponse)
def generate_test_case(request: PROverviewRequest):
    return review_service.generate_test_case(request)

@router.post('/risk-score', response_model=RiskScoreResponse)
def risk_score(request: PROverviewRequest):
    return review_service.get_risk_score(request)
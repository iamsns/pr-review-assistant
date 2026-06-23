from fastapi import APIRouter, Request

from schemas.review_request import PRRequest
from schemas.review_response import ReviewResponse, PROverview, PROverviewData
from services.review_service import ReviewService
from services.pr_overview_service import PROverviewService

review_router = APIRouter()

review_service = ReviewService()
review_service = PROverviewService()

@review_router.post('/overview', response_model=PROverviewData)
def review_pr(request: PRRequest):
    return review_service.generate_overview(request.pr_diff)

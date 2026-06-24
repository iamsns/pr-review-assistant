from fastapi import APIRouter, Request

from schemas.overview_schema import PROverviewData, PROverviewRequest
from services.review_service import ReviewService
from services.pr_overview_service import PROverviewService
from services.github_service import GithubService

overview_router = APIRouter()

review_service = ReviewService()
overview_service = PROverviewService()
github_service = GithubService()

@overview_router.post('/overview', response_model=PROverviewData)
def review_pr(request: PROverviewRequest):
    return overview_service.generate_overview(request)
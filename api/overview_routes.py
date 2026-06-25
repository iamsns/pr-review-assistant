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

@overview_router.post('/summary')
def pr_summary(request: PROverviewRequest):
    return overview_service.get_pr_summary(request)

@overview_router.post('/files_summary')
def pr_summary(request: PROverviewRequest):
    return overview_service.generate_file_summaries(request)
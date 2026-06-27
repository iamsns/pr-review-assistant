from fastapi import APIRouter
from api.overview_routes import overview_router
from api.review_routes import router as review_router

router = APIRouter()

router.include_router(router=overview_router, prefix="/pr")
router.include_router(router=review_router, prefix="/review")
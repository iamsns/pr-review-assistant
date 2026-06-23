from fastapi import APIRouter
from api.review import review_router

router = APIRouter()

router.include_router(router=review_router)
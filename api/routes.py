from fastapi import APIRouter
from api.overview_routes import overview_router

router = APIRouter()

router.include_router(router=overview_router)
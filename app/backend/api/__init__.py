from fastapi import APIRouter

from api.monitoring.health import router as health_router

router = APIRouter()

router.include_router(health_router, tags=["API Health"])

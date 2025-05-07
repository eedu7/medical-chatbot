from fastapi import APIRouter

from api.monitoring.health import router as health_router
from api.users import router as users_router

router = APIRouter()

router.include_router(health_router, tags=["API Health"])
router.include_router(users_router, tags=["Authentication"])

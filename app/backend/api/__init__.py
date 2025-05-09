from fastapi import APIRouter

from api.monitoring import router as health_router
from api.users import router as users_router
from api.auth import router as auth_router

router = APIRouter(prefix="/api")

router.include_router(health_router, prefix="/monitoring", tags=["API Health"])
router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
router.include_router(users_router,prefix="/users", tags=["User"])

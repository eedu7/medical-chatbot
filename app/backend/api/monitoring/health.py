from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from config import config

router = APIRouter()


@router.get("/health")
def health():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "OK",
            "status": "Health",
            "release_version": config.RELEASE_VERSION,
        },
    )

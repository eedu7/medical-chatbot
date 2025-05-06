from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/")
def index():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "OK",
            "title": "AI-Powered Multi-Cancer Detection and Medical Chatbot",
        },
    )

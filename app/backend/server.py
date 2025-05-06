from fastapi import FastAPI

from api import router


def init_routers(app_: FastAPI) -> None:
    app_.include_router(router)


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="AI-Powered Multi-Cancer Detection and Medical Chatbot",
        version="1.0.0",
    )
    init_routers(app_=app_)
    return app_


app: FastAPI = create_app()

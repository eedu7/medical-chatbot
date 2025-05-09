from typing import List

from fastapi import FastAPI
from fastapi.middleware import Middleware

from api import router
from middleware import SQLAlchemyMiddleware, AuthBackend, AuthenticationMiddleware


def init_routers(app_: FastAPI) -> None:
    app_.include_router(router)


def make_middleware() -> List[Middleware]:
    return [
        Middleware(SQLAlchemyMiddleware),
        Middleware(AuthenticationMiddleware, backend=AuthBackend),
    ]


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="AI-Powered Multi-Cancer Detection and Medical Chatbot",
        version="1.0.0",
        middleware=make_middleware(),
    )
    init_routers(app_=app_)

    return app_


app: FastAPI = create_app()

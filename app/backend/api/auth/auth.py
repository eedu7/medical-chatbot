from fastapi import APIRouter, Depends

from schemas.auth import AuthRegisterModel, AuthResponse
from dependencies.factory import Factory
from crud.auth import AuthCRUD

router = APIRouter()


@router.post("/auth/register", response_model=AuthResponse)
async def register(
    data: AuthRegisterModel, controller: AuthCRUD = Depends(Factory.get_auth_crud)
):
    return await controller.register(**data.model_dump())

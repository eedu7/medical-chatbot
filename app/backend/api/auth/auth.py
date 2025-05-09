from fastapi import APIRouter, Depends

from schemas.auth import AuthRegisterModel, AuthResponse, AuthLoginModel
from dependencies.factory import Factory
from crud.auth import AuthCRUD

router = APIRouter()


@router.post("/auth/register", response_model=AuthResponse)
async def register(
    data: AuthRegisterModel, controller: AuthCRUD = Depends(Factory.get_auth_crud)
):
    return await controller.register(
        username=data.username,
        email=data.email,
        password=data.password
    )

@router.post("/auth/login", response_model=AuthResponse)
async def login(data: AuthLoginModel, controller: AuthCRUD = Depends(Factory.get_auth_crud)):
    # TODO: Add the login logic
    ...
    
@router.post("/auth/logout")
async def logout():
    """
        TODO: Add the logout method, invalid the token,
        store the token in the redis database, and also delete the record after
        the jwt token expires.
    """
    ...
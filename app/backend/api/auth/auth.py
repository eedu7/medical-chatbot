from fastapi import APIRouter, Depends

from schemas.auth import AuthRegisterModel, AuthLoginModel
from schemas.token import Token
from dependencies.factory import Factory
from crud.auth import AuthCRUD

router = APIRouter()


@router.post(
    "/register",
)
async def register(
    data: AuthRegisterModel, controller: AuthCRUD = Depends(Factory.get_auth_crud)
):
    return await controller.register(
        username=data.username, email=data.email, password=data.password
    )


@router.post("/login", response_model=Token)
async def login(
    data: AuthLoginModel, controller: AuthCRUD = Depends(Factory.get_auth_crud)
) -> Token:
    return await controller.login(
        email=data.email,
        password=data.password,
    )


@router.post("/refresh-token")
async def refresh_token():
    # TODO: Implement logic to refresh JWT token and return a new access token
    ...


@router.post("/logout")
async def logout():
    """
    TODO: Implement logout logic:
    - Invalidate the current JWT token
    - Store it in Redis blacklist
    - Ensure Redis automatically deletes the record when the token expires
    """
    ...


@router.post("/forgot-password")
async def forgot_password():
    # TODO: Implement forgot password logic: send password reset link/token to user's email
    ...


@router.post("/reset-password")
async def reset_password():
    # TODO: Implement password reset logic: validate token and update the password
    ...


@router.post("/verify-email")
async def verify_email():
    # TODO: Implement email verification logic using token from query parameters
    ...

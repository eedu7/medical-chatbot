from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from schemas.auth import AuthRegisterModel, AuthLoginModel
from schemas.token import Token
from dependencies.factory import Factory
from crud.auth import AuthCRUD
from crud.user import UserCRUD

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


@router.get("/check-availability")
async def check_availability(
    username: str | None = None,
    email: str | None = None,
    controller: UserCRUD = Depends(Factory.get_user_crud),
) -> JSONResponse:
    if not username and not email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "message": "You must provide either a username or an email to check."
            },
        )

    if username:
        user = await controller.get_by_username(username)

        if user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail={"message": "Username is already taken."},
            )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "field": "username",
                "available": True,
                "message": "Username is available.",
            },
        )

    elif email:
        user = await controller.get_by_email(email)

        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"message": "Email is already registered"},
            )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "field": "email",
                "available": True,
                "message": "Email is available.",
            },
        )


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

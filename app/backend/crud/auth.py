from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from crud.base import BaseCRUD
from crud.user import UserCRUD
from models import User
from database import Transactional, Propagation
from utils import PasswordHandler, JWTHandler, TokenType
from schemas.token import Token
from config import config


class AuthCRUD(BaseCRUD[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(model=User, session=session)
        self.user_crud: UserCRUD = UserCRUD(session=session)

    @Transactional(propagation=Propagation.REQUIRED)
    async def register(self, username: str, email: str, password: str) -> User:
        email_exist = await self.user_crud.get_by_email(email)

        if email_exist:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    "message": f'User with the email "{email}" already exists.',
                },
            )

        username_exist = await self.user_crud.get_by_username(username)

        if username_exist:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    "message": f'User with the email "{username}" already exists.',
                },
            )

        hashed_password = PasswordHandler.hash_password(password)

        user = await self.create(
            {"username": username, "email": email, "password": hashed_password}
        )

        return user

    # TODO: Add the return of this method
    async def login(self, email: str, password: str) -> Token:
        from icecream import ic

        user = await self.user_crud.get_by_email(email)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"message": f'User with email "{email}" already exists.'},
            )

        if not PasswordHandler.verify_password(
            password=password, hashed_password=user.password
        ):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"message": "Invalid credentials"},
            )

        access_token_payload = {
            "user": {
                "uuid": str(user.uuid),
                "username": user.username,
                "email": user.email,
            },
            "type": "access",
        }

        refresh_token_payload = {"user_uuid": str(user.uuid), "type": "refresh"}

        # TODO: Create Access and Refresh Token
        access_token: str = JWTHandler.encode(
            payload=access_token_payload, token_type=TokenType.ACCESS_TOKEN
        )
        refresh_token: str = JWTHandler.encode(
            payload=refresh_token_payload, token_type=TokenType.REFRESH_TOKEN
        )

        return Token(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="bearer",
            expires_in=config.JWT_ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        )

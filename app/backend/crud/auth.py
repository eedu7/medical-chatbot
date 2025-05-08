from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from crud.base import BaseCRUD
from models import User
from database import Transactional, Propagation
from utils.password_handler import PasswordHandler


class AuthCRUD(BaseCRUD[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(model=User, session=session)

    @Transactional(propagation=Propagation.REQUIRED)
    async def register(self, username: str, email: str, password: str) -> User:
        email_exist = self.get_by(filters={"email": email})

        if email_exist:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    "message": f"User with the email {email} already exists.",
                },
            )

        username_exist = self.get_by(filters={"username": username})

        if username_exist:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    "message": f"User with the email {email} already exists.",
                },
            )

        hashed_password = PasswordHandler.hash_password(password)

        user = await self.create(
            {"username": username, "email": email, "password": hashed_password}
        )

        return user

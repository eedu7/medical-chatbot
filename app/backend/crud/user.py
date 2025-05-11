from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from crud.base import BaseCRUD
from models import User


class UserCRUD(BaseCRUD[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(model=User, session=session)

    async def get_by_email(self, email: str) -> User:
        try:
            return await self.get_by(filters={"email": email}, unique=True)
        except Exception as e:
            ...

    async def get_by_username(self, username: str) -> User:
        try:
            return await self.get_by(filters={"username": username}, unique=True)
        except Exception as e:
            ...

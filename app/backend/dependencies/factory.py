from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from crud.user import UserCRUD
from database import get_session


class Factory:
    @staticmethod
    def get_user_crud(session: AsyncSession = Depends(get_session)) -> UserCRUD:
        return UserCRUD(session=session)

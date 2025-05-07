from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from crud.base import BaseCRUD
from models import User


class AuthCRUD(BaseCRUD[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(model=User, session=session)

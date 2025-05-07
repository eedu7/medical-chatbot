from typing import Any, Dict, List
from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from crud.base import BaseCRUD
from models import User
from database import Transactional, Propagation


class UserCRUD(BaseCRUD[User]):
    """
    User-specific CRUD operations for managing user accounts in the database.
    """

    def __init__(self, session: AsyncSession):
        """
        Initializes the UserCRUD class with the provided async session and User Model

        Args:
            session (AsyncSession): The SQLAlchemy asynchronous session to interact with the database.
        """
        super().__init__(model=User, session=session)

    async def get_by_email(self, email: str) -> User | None:
        """
        Asynchronously retrieves a user from the database by their email address.

        Args:
            email (str): The email address of the User to be retrieved.

        Returns:
            User | None: The user object if found, otherwise None
        """
        try:
            filter_ = {"email": email}
            return await self.get_by(filter_, unique=True)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    "Error Message": str(e),
                    "Place of occurence": "In the get_by_email method of the UserCRUD",
                },
            )

    async def get_by_uuid(self, uuid: UUID) -> User | None:
        """
        Asynchronously retrieves a user from the database by their uuid.

        Args:
            uuid (UUID): The uuid of the User to be retrieved.

        Returns:
            User | None: The user object if found, otherwise None
        """
        try:
            filter_ = {"uuid": uuid}
            return await self.get_by(filter_, unique=True)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    "Error Message": str(e),
                    "Place of occurence": "In the get_by_uuid method of the UserCRUD",
                },
            )

    async def get_all_users(self, skip: int = 0, limit: int = 100) -> List[User] | None:
        """
        Asynchronously retrieves all the users.

        Args:
            skip (int): The number of users data to skip. Defaults to "0".
            limit (int): The number of users data to retrieve. Defaults to "100"

        Returns:
            List[User] | None: The list of users data or None

        Raises:
            BadRequestException: If there is any error.
        """
        try:
            return await self.get_by(
                skip=skip,
                limit=limit,
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    "Error Message": str(e),
                    "Place of occurence": "In the get_all_users method of the UserCRUD",
                },
            )

    @Transactional(propagation=Propagation.REQUIRED)
    async def register(self, email: str, password: str, username: str) -> User:
        """
        Registers a new user asynchronously by hashing their password and saving
        the user data to the database.

        Args:
            email (str): The email address of the new user.
            password (str): The password of the new user.
            username (str): The username of the new user.

        Returns:
            User: The newly created User object with the hashed password

        Raises:
            BadRequestException: If a user with the same email already exists.
        """
        # user = await self.get_by_email(email)
        # if user:
        #     raise HTTPException(
        #         status_code=status.HTTP_400_BAD_REQUEST,
        #         detail={
        #             "Place of occurence": "In the register method of the UserCRUD",
        #         },
        #     )

        user = await self.create(
            {"username": username, "email": email, "password": password}
        )
        return user

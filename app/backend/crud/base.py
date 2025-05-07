from typing import Any, Dict, Generic, Sequence, Type, TypeVar
from uuid import UUID

from fastapi import HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import and_, select

from database import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseCRUD(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], session: AsyncSession) -> None:
        self.model = model
        self.session = session

    async def get_by(
        self,
        filters: Dict[str, Any] | None = None,
        *,
        unique: bool = False,
        skip: int = 0,
        limit: int = 10,
        order_by: str | None = None,
        order_desc: bool = False,
    ) -> Sequence[ModelType] | ModelType | None:
        try:
            query = select(self.model)

            if filters:
                conditions = []

                for field, value in filters.items():
                    conditions.append(getattr(self.model, field) == value)
                query = query.where(and_(*conditions))
            query = query.offset(skip).limit(limit)

            if order_by:
                order_column = getattr(self.model, order_by)
                query = query.order_by(
                    order_column.desc() if order_desc else order_column.asc()
                )

            result = await self.session.execute(query)

            if unique:
                return result.scalar().first()

            return result.scalars().all()
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail={
                    "Error Message": str(e),
                    "Place of occurence": "In the get_by method of the BaseCRUD",
                },
            )

    async def get_by_uuid(self, uuid: UUID | str) -> ModelType | None:
        try:
            return await self.get_by(filters={"uuid": uuid}, unique=True)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail={
                    "Error Message": str(e),
                    "Place of occurence": "In the get_by_uuid method of the BaseCRUD",
                },
            )

    async def create(self, attributes: Dict[str, Any]) -> ModelType:
        try:
            model = self.model(**attributes)
            self.session.add(model)
            await self.session.commit()
            return model

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail={
                    "Error Message": str(e),
                    "Place of occurence": "In the create method of the BaseCRUD",
                },
            )

    async def update(self, model: ModelType, attributes: Dict[str, Any]) -> bool:
        try:
            for key, value in attributes.items():
                setattr(model, key, value)
            await self.session.commit()
            return True

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail={
                    "Error Message": str(e),
                    "Place of occurence": "In the update method of the BaseCRUD",
                },
            )

    async def delete(self, model: ModelType) -> bool:
        try:
            await self.session.delete(model)
            await self.session.commit()
            return True
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail={
                    "Error Message": str(e),
                    "Place of occurence": "In the delete method of the BaseCRUD",
                },
            )

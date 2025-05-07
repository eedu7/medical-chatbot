from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID, Unicode
from sqlalchemy.orm import Mapped, mapped_column

from database import Base
from database.mixins import TimeStampMixin


class User(Base, TimeStampMixin):
    __tablename__ = "users"

    uuid: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid4
    )
    username: Mapped[str] = mapped_column(
        Unicode(32), unique=True, nullable=False, index=True
    )
    email: Mapped[str] = mapped_column(
        Unicode(320), unique=True, nullable=False, index=True
    )
    password: Mapped[str] = mapped_column(Unicode(128), nullable=False)

    def __str__(self):
        return f"uuid: {self.uuid}, username: {self.username}, email: {self.email}"

    def __repr__(self):
        return self.__str__()

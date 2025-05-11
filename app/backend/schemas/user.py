from uuid import UUID
from pydantic import BaseModel, Field


class CurrentUser(BaseModel):
    uuid: UUID | None = Field(None, description="User's UUID")

    class Config:
        validate_assignment = True

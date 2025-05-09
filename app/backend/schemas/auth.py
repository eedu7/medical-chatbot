import re
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field, field_validator


class AuthBase(BaseModel):
    email: EmailStr
    password: str = Field(..., examples=["Password@123"])

    @field_validator("password")
    def password_must_contain_special_characters(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")

        if not re.search(r"[^a-zA-z0-9]", v):
            raise ValueError("Password must contain special characters")
        if not re.search(r"[0-9]", v):
            raise ValueError("Password must contain numbers")
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain uppercase characters")
        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain lowercase characters")
        return v


class AuthLoginModel(AuthBase):
    pass


class AuthRegisterModel(AuthBase):
    username: str = Field(..., min_length=3, max_length=18)

    @field_validator("username")
    def username_must_not_contain_special_characters(cls, v: str) -> str:
        if re.search(r"[^a-zA-Z0-9]", v):
            raise ValueError("Username must not contain special characters")
        if v.isdigit():
            raise ValueError("Username cannot be only nubmers")
        return v


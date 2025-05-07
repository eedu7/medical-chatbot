import re
from pydantic import BaseModel, EmailStr, SecretStr, Field, field_validator


class AuthBase(BaseModel):
    email: EmailStr
    password: SecretStr

    @field_validator("password")
    def password_must_contain_special_characters(cls, v: SecretStr) -> SecretStr:
        password = v.get_secret_value()

        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")

        if not re.search(r"[^a-zA-z0-9]", password):
            raise ValueError("Password must contain special characters")
        if not re.search(r"[0-9]", password):
            raise ValueError("Password must contain numbers")
        if not re.search(r"[A-Z]", password):
            raise ValueError("Password must contain uppercase characters")
        if not re.search(r"[a-z]", password):
            raise ValueError("Password must contain lowercase characters")
        return v


class UserLoginModel(AuthBase):
    pass


class UserRegisterModel(AuthBase):
    username: str = Field(..., min_length=8, max_length=64)

    @field_validator("username")
    def username_must_not_contain_special_characters(cls, v: str) -> str:
        if re.search(r"[^a-zA-Z0-9]", v):
            raise ValueError("Username must not contain special characters")
        if v.isdigit():
            raise ValueError("Username cannot be only nubmers")
        return v

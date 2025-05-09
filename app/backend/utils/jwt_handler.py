from uuid import uuid4
from typing import Any, Dict
from datetime import timedelta
from enum import StrEnum

from fastapi import HTTPException, status
from jose import ExpiredSignatureError, JWTError, jwt

from config import config
from .current_datetime import get_current_datetime


class TokenType(StrEnum):
    ACCESS_TOKEN = "access_token"
    REFRESH_TOKEN = "refresh_token"


class JWTHandler:
    secret_key: str = config.JWT_SECRET_KEY
    algorithm: str = config.JWT_ALGORITHM
    access_expire_minutes: int = config.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    refresh_expire_minutes: int = config.JWT_REFRESH_TOKEN_EXPIRE_MINUTES

    @classmethod
    def encode(
        cls,
        payload: Dict[str, Any],
        token_type: TokenType = TokenType.ACCESS_TOKEN,
    ) -> str:
        time_of_encoding = get_current_datetime()

        if token_type == TokenType.ACCESS_TOKEN:
            expire = time_of_encoding + timedelta(minutes=cls.access_expire_minutes)
        elif token_type == TokenType.REFRESH_TOKEN:
            expire = time_of_encoding + timedelta(minutes=cls.refresh_expire_minutes)

        jti = str(uuid4())

        payload.update({"exp": expire, "jti": jti, "iat": time_of_encoding})

        return jwt.encode(payload, cls.secret_key, algorithm=cls.algorithm)

    @classmethod
    def decode(cls, token: str) -> Dict[str, Any]:
        try:
            return jwt.decode(token, cls.secret_key, algorithms=[cls.algorithm])
        except ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail={"message": "Expired token"},
            )

        except JWTError as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail={"message": "Invalid token"},
            )
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail={
                    "message": "Invalid token",
                },
            )

    @classmethod
    def decode_expired(cls, token: str) -> Dict[str, Any]:
        try:
            return jwt.decode(
                token,
                cls.secret_key,
                algorithms=[cls.algorithm],
                options={"verify_exp": False},
            )
        except JWTError as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail={"message": "Invalid token"},
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail={"message": "Invalid token"},
            )

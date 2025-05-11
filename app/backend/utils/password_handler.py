from passlib.context import CryptContext


class PasswordHandler:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def hash_password(cls, password: str) -> str:
        if not isinstance(password, str) or not password.strip():
            raise ValueError("Password must be a non-empty string.")
        return cls.pwd_context.hash(password)

    @classmethod
    def verify_password(cls, password: str, hashed_password: str) -> bool:
        if not isinstance(password, str) or not password.strip():
            raise ValueError("Password must be a non-empty string.")
        if not isinstance(hashed_password, str) or not hashed_password.strip():
            raise ValueError("Hashed Password must be a non-empty string.")
        return cls.pwd_context.verify(password, hashed_password)

from pydantic import BaseModel, Field


class Token(BaseModel):
    access_token: str = Field(
        ..., description="JWT access token used for authenticating user requests."
    )
    refresh_token: str = Field(
        ...,
        description="Token used to obtain a new access token after the current one expires.",
    )
    token_type: str = Field(
        ..., description="Type of the token issued.", examples=["bearer"]
    )
    expires_in: int = Field(
        ...,
        description="Duration in seconds until the access token expires.",
        example=[3600],
    )

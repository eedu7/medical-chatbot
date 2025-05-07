from fastapi import APIRouter, Depends

from crud.user import UserCRUD
from dependencies.factory import Factory

router = APIRouter()


@router.get("/")
async def get_users(
    controller: UserCRUD = Depends(Factory().get_user_crud),
):
    users = await controller.get_all()

    return users


from pydantic import BaseModel


class RegisterForm(BaseModel):
    username: str
    email: str
    password: str


@router.post("/", status_code=201)
async def register_user(
    form: RegisterForm,
    controller: UserCRUD = Depends(Factory().get_user_crud),
):
    return await controller.register(
        email=form.email,
        password=form.password,
        username=form.username,
    )

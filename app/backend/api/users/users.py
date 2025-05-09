from fastapi import APIRouter, Depends, Request

from crud.user import UserCRUD
from dependencies.authentication import AuthenticationRequired
from dependencies.factory import Factory

router = APIRouter()


@router.get("/profile", dependencies=[Depends(AuthenticationRequired)])
async def get_user_profile(
    request: Request, controller: UserCRUD = Depends(Factory.get_user_crud)
):
    return await controller.get_by_uuid(request.user.uuid)


@router.put("/profile")
async def update_user_profile():
    # TODO: Implement logic to update the current user's profile with the provided data
    ...


@router.patch("/profile")
async def update_user_profile():
    # TODO: Implement logic to update the current user's profile with the provided data
    ...

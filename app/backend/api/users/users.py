from fastapi import APIRouter, Request, Depends

from crud.user import UserCRUD
from dependencies.authentication import AuthenticationRequired
from dependencies.factory import Factory

router = APIRouter()


@router.get("/profile")
async def get_user_profile():
    # TODO: Implement logic to retrieve and return the current user's profile data

    ...


@router.put("/profile", dependencies=[Depends(AuthenticationRequired)])
async def update_user_profile(
    request: Request, controller: UserCRUD = Depends(Factory.get_user_crud)
):
    return await controller.get_by_uuid(request.user.uuid)

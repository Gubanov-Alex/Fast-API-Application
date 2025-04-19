from fastapi import APIRouter
from models import User

user_router = APIRouter(prefix="/users", tags=["Users"])




@user_router.get("/{users_id}")
async def get_user(users_id: int):
    return {"message": f"Hello {users_id}"}


@user_router.get("/")
async def get_users():
    return {"message": "Hello Users"}


@user_router.post("/")
async def create_user(user: User):
    return {"message": f"Hello {user}"}


@user_router.put("/{users_id}")
async def update_user(users_id: int):
    return {"message": f"Refresh {users_id}"}


@user_router.delete("/{users_id}")
async def delete_user(users_id: int):
    return {"message": f"Bye Bye {users_id}"}

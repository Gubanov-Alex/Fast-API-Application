from fastapi import FastAPI

from models import User
from API.users import user_router

from fastapi import APIRouter

v1_router = APIRouter(prefix="/v1",tags=["v1"])
v2_router = APIRouter(prefix="/v2",tags=["v2"])

v1_router.include_router(user_router)
v2_router.include_router(user_router)

app = FastAPI()
app.include_router(v1_router)
app.include_router(v2_router)


# =====Quary parametrs===========
@app.get("/")
async def read_root(name: str, age: int):
    return {f"Hello:{name}, your age is:{age}"}

# ====== Body parametrs=============

# @app.post("/post")
# async def post_root(user: User,user2:User, age_user: int, age_user2: int ):
#     return {f"Hello:{user.name},{user2.name} your overall age is:{age_user+age_user2}"}

@app.post("/post")
async def post_root(users:list[User] = None):
    if users is None:
        return {"Hello: No users"}
    else:
        names = [user.name for user in users]
    return {f"Hello: {",".join(names)}"}

# ========== Path parametrs============

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
from contextlib import asynccontextmanager
from datetime import time,datetime
from urllib.request import Request
from asyncio import sleep

import uvicorn
from typing import Optional
from fastapi import FastAPI, Response, Depends, BackgroundTasks


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("App starting up...")
    yield
    print("App shutting down...")

app = FastAPI(lifespan=lifespan)

async def very_slow_func():
    await sleep(5)

@app.get("/slow_func")
async def slow_func(background_task: BackgroundTasks):
    background_task.add_task(very_slow_func)
    return {"message": "hello world"}



def paginate(limit:Optional[int] = 10, offset:Optional[int] = 0)-> dict:
    return {
        "limit":limit,
        "offset":offset,
    }

@app.get("/users")
async def get_users(pagination: dict= Depends(paginate)):
    now = datetime.now()
    users = [
        {
            "name":"Sasha",
            "is_online":True,
        },
        {
            "name":"Fara",
            "is_online":True,
        }

    ]
    responce_time = datetime.now() - now
    print(responce_time)
    return users[pagination["offset"] :pagination["offset"] + pagination["limit"]]

@app.get("/chats")
async def get_chats():
    chats = [
        {
            "name":"chat_1",
            "members":2,
        },
        {
            "name":"chat_2",
            "members":1,
        }

    ]
    return chats

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    now = datetime.now()
    response = await call_next(request)
    response.headers["X-Process-Time"] = str(datetime.now()-now)
    return response






if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
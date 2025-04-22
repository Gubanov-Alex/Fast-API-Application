import uvicorn
from fastapi import FastAPI, Response
from pydantic import BaseModel
from starlette.responses import JSONResponse, FileResponse, StreamingResponse
from starlette.websockets import WebSocket
import logging

logger = logging.getLogger(__name__)
app = FastAPI()

USERS = {}

def generator():
    yield "Hello, World!"



class ResponseExample(BaseModel):
    message: str

@app.get("/", response_model=ResponseExample)
async def root(response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.set_cookie(key="token", value="<PASSWORD>", max_age=3600)
    return {"message": "Hello World"}

# @app.get("/", response_model=ResponseExample)
# async def root():
#     responce = JSONResponse({"message": "Hello World","message2": "Hello World"}, headers={"X-Cat": "MEOW"})
#     responce.set_cookie(key="message", value="Hello World", max_age=3600)
#     return responce

# @app.get("/", response_model=ResponseExample)
# async def root():
#     return JSONResponse({"message": "Hello World","message2": "Hello World"}, headers={"X-Cat": "MEOW"})


# @app.get("/", response_model=ResponseExample)
# async def root():
#     return ({"message": "Hello World","message2": "Hello World"}


# @app.get("/")
# async def root():
#     return StreamingResponse(generator())
    # return FileResponse("/home/oleksandr/PycharmProjects/Fast-API-Application/README.md")
    # return JSONResponse(content= "message: Hello World", status_code=202)

@app.get("/hello/{name}")
async def hello(name: str):
    return {"message": f"Hello, {name}!"}


@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    name = await websocket.receive_text()
    USERS[name] = websocket
    while True:
        data = await websocket.receive_text()
        if USERS["Sasha"]:
            await USERS["Fara"].send_text(data)
        else:
            await USERS["Sasha"].send_text(data)




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
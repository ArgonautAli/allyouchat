from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine
from users.router import router as users_router


app = FastAPI()

models.Base.metadata.create_all(bind = engine)


## This is to define prefix
# main_router = APIRouter(prefix="/allyouchat")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(users_router)

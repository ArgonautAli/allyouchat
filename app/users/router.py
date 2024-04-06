from fastapi import APIRouter, Query, Request
from fastapi.responses import JSONResponse
from sqlalchemy import select
from models import User
from classes import UserBase
from uuid import uuid4
from database import db_dependency

router = APIRouter(prefix="/user")



@router.post("/create")
async def create_user(req: Request, body: UserBase,):
    username = body.user_name
    userid = uuid4()
    return {"username": username, "id": userid}

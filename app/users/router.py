from fastapi import APIRouter, Query, Request
from fastapi.responses import JSONResponse
from sqlalchemy import select
from classes import UserBase
from uuid import uuid4
from database import db_dependency, db
import models

router = APIRouter(prefix="/user")



@router.post("/create")
async def create_user(req: Request, body: UserBase):
    user_name = body.user_name
    user_id = uuid4()
    user: UserBase = {"user_name": user_name,"id": user_id}
    db_user = models.User(**user)
    db.add(db_user)
    db.commit()
    return {"user_id": user_id}

@router.get("/getuser/{user_id}")
async def read_user(req: Request, user_id: int, db: db_dependency):
    user = db.query(models.User).filter(models.user.id == user_id).first()
    return {"user": user.user_name}
    

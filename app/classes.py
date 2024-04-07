from pydantic import BaseModel, UUID4
from typing import List, Optional

class MessageBase(BaseModel):
    sender_id: str
    recipient_id: str
    content: str

class UserBase(BaseModel):
    user_name: str

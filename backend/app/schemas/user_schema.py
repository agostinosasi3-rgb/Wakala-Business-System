from pydantic import BaseModel
from datetime import datetime
from app.models.user import UserRole

class UserBase(BaseModel):
    full_name: str
    username: str
    phone_number: str
    role: UserRole = UserRole.AGENT

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse
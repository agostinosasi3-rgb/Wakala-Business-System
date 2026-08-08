from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.user import User
from app.schemas.user_schema import UserCreate
from app.core.security import SecurityManager

class AuthService:
    def __init__(self, db: Session):
        self.db = db

    def register_user(self, user_data: UserCreate) -> User:
        existing_user = self.db.query(User).filter(
            (User.username == user_data.username) | (User.phone_number == user_data.phone_number)
        ).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username au Namba ya simu ipo tayari kwenye mfumo."
            )
        
        hashed_pwd = SecurityManager.get_password_hash(user_data.password)
        new_user = User(
            full_name=user_data.full_name,
            username=user_data.username,
            phone_number=user_data.phone_number,
            hashed_password=hashed_pwd,
            role=user_data.role
        )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def authenticate_user(self, username: str, password: str) -> User:
        user = self.db.query(User).filter(User.username == username).first()
        if not user or not SecurityManager.verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Username au Password siyo sahihi."
            )
        return user
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from pydantic import BaseModel 
from . db import get_session 
from user import User 

router = APIRouter()

class SignupRequest(BaseModel):
    username: str 
    email: str 
    password: str

class LoginRequest(BaseModel):
    username: str 
    password: str

@router.post("/signup")
async def signup(user_data: SignupRequest, session: Session = Depends(get_session)):
    existing_user = session.exec(
        select(User).where(User.username == user_data.username)).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists.")

    hashed_password = User.hash_password(user_data.password)
    new_user = User(
        username=user_data.username,
        email = user_data.email,
        hashed_password=hashed_password
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return {"message": "User created", "user_id": new_user.id}

@router.post("/login")
async def login(login_data: LoginRequest, session: Session = Depends(get_session)):
    user = session.exec(
        select(User).where(User.username == login_data.username)).first()
    if not user or not user.verify_password(login_data.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    # TODO: Refactor to return a token 
    return {"message"}

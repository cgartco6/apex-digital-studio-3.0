from fastapi import APIRouter, Depends
from passlib.context import CryptContext
from app.database.session import SessionLocal
from app.models.user import User
from app.auth.jwt import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register")
def register(email: str, password: str):
    db = SessionLocal()
    hashed = pwd_context.hash(password)
    user = User(email=email, hashed_password=hashed)
    db.add(user)
    db.commit()
    return {"status": "created"}

@router.post("/login")
def login(email: str, password: str):
    db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()
    if not user or not pwd_context.verify(password, user.hashed_password):
        return {"error": "invalid credentials"}
    token = create_access_token({"sub": user.id})
    return {"access_token": token, "token_type": "bearer"}

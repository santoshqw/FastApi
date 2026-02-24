from fastapi import APIRouter, Depends, Response, HTTPException
from sqlalchemy.orm import Session

from schema.userSchema import UserCreate, UserLogin
from services.auth_service import create_user, authenticate_user
from db.database import get_db
from core.security import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

# SIGNUP
@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    try:
        new_user = create_user(db, user)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return {"message": "User created", "user": new_user.email}


# LOGIN (SET COOKIE)
@router.post("/login")
def login(user: UserLogin, response: Response, db: Session = Depends(get_db)):

    db_user = authenticate_user(db, user.email, user.password)

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": db_user.email})

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,   # JS cannot access
        samesite="lax"
    )

    return {"message": "Login successful"}


# LOGOUT (DELETE COOKIE)
@router.post("/logout")
def logout(response: Response):
    response.delete_cookie("access_token")
    return {"message": "Logged out"}
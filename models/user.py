from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: str = Field(..., min_length=5, max_length=100)
    password:str =Field(...,min_length=6 ,max_length=16)


class User(UserCreate):
    id: int
    is_active: bool = True

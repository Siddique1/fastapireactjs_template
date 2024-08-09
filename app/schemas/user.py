from pydantic import BaseModel, EmailStr
from typing import List, Optional

class RoleBase(BaseModel):
    name: str

class RoleCreate(RoleBase):
    pass

class RoleUpdate(RoleBase):
    pass

class Role(RoleBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False

class UserCreate(UserBase):
    password: str
    roles: List[Role] = []

class UserUpdate(UserBase):
    password: Optional[str] = None
    roles: List[Role] = []

class UserInDBBase(UserBase):
    id: int
    roles: List[Role] = []

    class Config:
        orm_mode = True

class User(UserInDBBase):
    pass

    #########

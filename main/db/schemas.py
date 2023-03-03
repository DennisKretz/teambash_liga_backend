from typing import List, Union
from pydantic import BaseModel

class UserBase(BaseModel):

    username: str

class UserLogin(UserBase):

    username: str
    password: str

class UserCreate(UserBase):

    password: str

class User(UserBase):

    id: int
    is_active: bool
    role: str

    class Config:
        
        orm_mode = True

################ ROLES ################
class RoleBase(BaseModel):

    name: str

class RoleCreate(RoleBase):

    can_view_routes: list

class Role(RoleBase):

    id: int
    level: int
    can_ban: bool
    can_support: bool
    can_manage: bool

    class Config:

        orm_mode = True
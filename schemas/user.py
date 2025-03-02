from pydantic import BaseModel
import datetime

class UserBase(BaseModel):
    username: str
    first_name: str
    middle_initial: str
    last_name: str
    email: str
    date_of_birth: datetime.date
    address: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
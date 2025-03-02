from fastapi import FastAPI, HTTPException, Depends, status
from typing import Annotated, List
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import models
from fastapi.middleware.cors import CORSMiddleware

from schemas import UserModel, UserBase

app = FastAPI()

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

models.Base.metadata.create_all(bind=engine)

@app.post("/users/", response_model=UserModel)
async def create_user(user: UserBase, db: db_dependency):
    user = models.User(**user.model_dump())
    db.add(user)
    db.commit()

@app.get("/users", response_model=List[UserModel])
async def read_users(db: db_dependency, skip: int = 0, limit: int = 100):
    db_users = db.query(models.User).offset(skip).limit(limit).all()
    if not db_users:
        raise HTTPException(status_code=404, detail='No users found.')
    return db_users

@app.get("/users/{user_id}", response_model=UserModel)
async def read_user(user_id: int, db: db_dependency):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found.')
    return db_user

@app.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int, db: db_dependency):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found.')
    db.delete(db_user)
    db.commit()
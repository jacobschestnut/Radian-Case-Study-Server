from fastapi import FastAPI, HTTPException, Depends, status
from typing import Annotated
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import models
from fastapi.middleware.cors import CORSMiddleware

from schemas import UserBase

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

@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    user = models.User(**user.model_dump())
    db.add(user)
    db.commit()

@app.get("/users", status_code=status.HTTP_200_OK)
async def read_users(db: db_dependency):
    db_users = db.query(models.User).all()
    if not db_users:
        raise HTTPException(status_code=404, detail='No users found.')
    return db_users

@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def read_user(user_id: int, db: db_dependency):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found.')
    return db_user

@app.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int, db: db_dependency):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail='User was not found.')
    db.delete(db_user)
    db.commit()
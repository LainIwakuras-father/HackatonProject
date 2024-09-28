from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

import crud
from database import get_db
from schemas import User, Task, TaskCreate, UserCreate

router = APIRouter()

@router.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@router.get("/users/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users/{user_id}/task/", response_model=Task)
def create_task_for_user(
    user_id: int, task: TaskCreate, db: Session = Depends(get_db)
):
    return crud.create_use_task(db=db, task=task, user_id=user_id)


@router.get("/task/", response_model=list[Task])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    task = crud.get_task(db, skip=skip, limit=limit)
    return task
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.user import UserCreate, UserUpdate, User
from app.crud.user import (
    create_user,
    get_user,
    get_user_by_email,
    update_user,
    delete_user,
)
from app.db.session import get_db
from app.core.security import get_current_active_user, get_current_active_superuser

router = APIRouter()




@router.post("/users/", response_model=User)
async def create_new_user(user: UserCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_active_superuser)):
    db_user = await get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    return await create_user(db, user)


@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    db_user = await get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user


@router.put("/users/{user_id}", response_model=User)
async def update_existing_user(user_id: int, user: UserUpdate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_active_superuser)):
    db_user = await get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return await update_user(db, db_user, user)


@router.delete("/users/{user_id}", response_model=User)
async def delete_existing_user(user_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_active_superuser)):
    db_user = await delete_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user




from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.user import Role, RoleCreate, RoleUpdate
from app.crud.role import (
    get_role,
    get_role_by_name,
    get_roles,
    create_role,
    update_role,
    delete_role,
)
from app.db.session import get_db
from app.core.security import get_current_active_superuser

router = APIRouter()


@router.post("/roles/", response_model=Role)
async def create_new_role(
    role: RoleCreate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_active_superuser),
):
    db_role = await get_role_by_name(db, role.name)
    if db_role:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Role already exists"
        )
    return await create_role(db, role)


@router.get("/roles/", response_model=List[Role])
async def read_roles(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_active_superuser),
):
    return await get_roles(db, skip=skip, limit=limit)


@router.get("/roles/{role_id}", response_model=Role)
async def read_role(
    role_id: int,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_active_superuser),
):
    db_role = await get_role(db, role_id)
    if not db_role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Role not found"
        )
    return db_role


@router.put("/roles/{role_id}", response_model=Role)
async def update_existing_role(
    role_id: int,
    role: RoleUpdate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_active_superuser),
):
    db_role = await get_role(db, role_id)
    if not db_role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Role not found"
        )
    return await update_role(db, db_role, role)


@router.delete("/roles/{role_id}", response_model=Role)
async def delete_existing_role(
    role_id: int,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_active_superuser),
):
    db_role = await delete_role(db, role_id)
    if not db_role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Role not found"
        )
    return db_role

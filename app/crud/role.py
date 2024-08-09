from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import Role
from app.schemas.user import RoleCreate, RoleUpdate


async def get_role(db: AsyncSession, role_id: int):
    result = await db.execute(select(Role).filter(Role.id == role_id))
    return result.scalar_one_or_none()


async def get_role_by_name(db: AsyncSession, role_name: str):
    result = await db.execute(select(Role).filter(Role.name == role_name))
    return result.scalar_one_or_none()


async def get_roles(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Role).offset(skip).limit(limit))
    return result.scalars().all()


async def create_role(db: AsyncSession, role: RoleCreate):
    db_role = Role(name=role.name)
    db.add(db_role)
    await db.commit()
    await db.refresh(db_role)
    return db_role


async def update_role(db: AsyncSession, db_role: Role, role_update: RoleUpdate):
    update_data = role_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_role, key, value)
    await db.commit()
    await db.refresh(db_role)
    return db_role


async def delete_role(db: AsyncSession, role_id: int):
    role = await get_role(db, role_id)
    if role:
        await db.delete(role)
        await db.commit()
        return role
    return None

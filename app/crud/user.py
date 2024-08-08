from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


from app.models.user import User, Role
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import verify_password, get_password_hash

async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).filter(User.id == user_id))
    print(result)
    return result.scalar_one_or_none()


async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).filter(User.email == email))
    return result.scalar_one_or_none()


async def create_user(db: AsyncSession, user: UserCreate):
    db_user = User(email=user.email, hashed_password=get_password_hash(user.password))
    db_user.roles = [await get_or_create_role(db, role.name) for role in user.roles]
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def update_user(db: AsyncSession, db_user: User, user_update: UserUpdate):
    update_data = user_update.dict(exclude_unset=True)
    if "password" in update_data and update_data["password"]:
        db_user.hashed_password = get_password_hash(update_data["password"])
    if "roles" in update_data:
        db_user.roles = [await get_or_create_role(db, role.name) for role in update_data["roles"]]
    for key, value in update_data.items():
        if key not in ["password", "roles"]:
            setattr(db_user, key, value)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def delete_user(db: AsyncSession, user_id: int):
    user = await get_user(db, user_id)
    if user:
        await db.delete(user)
        await db.commit()
        return user
    return None


async def get_or_create_role(db: AsyncSession, role_name: str):
    result = await db.execute(select(Role).filter(Role.name == role_name))
    role = result.scalar_one_or_none()
    if not role:
        role = Role(name=role_name)
        db.add(role)
        await db.commit()
        await db.refresh(role)
    return role





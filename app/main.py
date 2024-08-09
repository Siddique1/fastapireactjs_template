from fastapi import FastAPI
from app.api import user, role

app = FastAPI()

app.include_router(user.router, prefix="/api", tags=["users"])
app.include_router(role.router, prefix="/api", tags=["roles"])

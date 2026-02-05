from fastapi import FastAPI
app = FastAPI(title="Apex Digital Studio")
from .api.v1.endpoints import router
app.include_router(router, prefix="/api/v1")
from app.api.v1 import auth
app.include_router(auth.router)
from app.api.v1 import ai
app.include_router(ai.router)
from app.api.v1 import billing
app.include_router(billing.router)
from app.api.v1 import admin
app.include_router(admin.router)

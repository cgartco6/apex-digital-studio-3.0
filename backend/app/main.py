from fastapi import FastAPI
from .api.v1.endpoints import router
from app.api.v1 import auth
app.include_router(auth.router)
from app.api.v1 import ai
app.include_router(ai.router)
from app.api.v1 import billing
app.include_router(billing.router)

app = FastAPI(title="Apex Digital Studio")
app.include_router(router, prefix="/api/v1")

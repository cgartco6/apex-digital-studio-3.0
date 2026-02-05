from fastapi import FastAPI
from .api.v1.endpoints import router

app = FastAPI(title="Apex Digital Studio")
app.include_router(router, prefix="/api/v1")

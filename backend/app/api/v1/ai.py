from fastapi import APIRouter, Depends
from app.ai_core.execution_engine import ExecutionEngine
from app.auth.dependencies import get_current_user

router = APIRouter(prefix="/ai", tags=["ai"])
engine = ExecutionEngine()

@router.post("/run")
def run_ai(prompt: str, user=Depends(get_current_user)):
    return {"result": engine.execute(prompt, str(user.id))}

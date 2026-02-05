from fastapi import APIRouter, Depends
from app.auth.permissions import require_admin
from app.admin.metrics import AdminMetrics
from app.database.session import SessionLocal
from app.models.user import User

router = APIRouter(prefix="/admin", tags=["admin"])
metrics = AdminMetrics()

@router.get("/metrics")
def system_metrics(admin=Depends(require_admin)):
    return metrics.snapshot()

@router.get("/users")
def list_users(admin=Depends(require_admin)):
    db = SessionLocal()
    return db.query(User).all()

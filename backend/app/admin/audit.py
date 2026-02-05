from app.database.session import SessionLocal
from app.models.audit_log import AuditLog

class AuditService:
    def log(self, user_id, action, metadata=""):
        db = SessionLocal()
        entry = AuditLog(user_id=user_id, action=action, metadata=metadata)
        db.add(entry)
        db.commit()

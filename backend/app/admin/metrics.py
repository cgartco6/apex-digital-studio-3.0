from app.database.session import SessionLocal
from app.models.user import User
from app.models.subscription import Subscription

class AdminMetrics:
    def snapshot(self):
        db = SessionLocal()
        return {
            "users": db.query(User).count(),
            "subscriptions": db.query(Subscription).count()
        }

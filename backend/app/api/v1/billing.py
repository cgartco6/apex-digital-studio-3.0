from fastapi import APIRouter, Depends
from app.billing.stripe_service import StripeService
from app.billing.payfast_service import PayFastService
from app.auth.dependencies import get_current_user

router = APIRouter(prefix="/billing", tags=["billing"])
stripe_service = StripeService()
payfast_service = PayFastService()

@router.post("/stripe/checkout")
def stripe_checkout(price_id: str, user=Depends(get_current_user)):
    return {"url": stripe_service.create_checkout(price_id)}

@router.post("/payfast/checkout")
def payfast_checkout(amount: float, user=Depends(get_current_user)):
    data = {"amount": amount, "item_name": "Apex Subscription"}
    return {"url": payfast_service.generate_payment_url(data)}

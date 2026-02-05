from fastapi import APIRouter, Request
import stripe, os

router = APIRouter(prefix="/billing/webhooks")

@router.post("/stripe")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig = request.headers.get("stripe-signature")
    stripe.Webhook.construct_event(payload, sig, os.getenv("STRIPE_WEBHOOK_SECRET"))
    return {"status": "ok"}

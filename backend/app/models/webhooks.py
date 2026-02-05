from fastapi import APIRouter, Request
import stripe, os

router = APIRouter(prefix="/billing/webhooks")

@router.post("/stripe")

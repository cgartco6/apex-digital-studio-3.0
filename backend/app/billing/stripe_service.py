import stripe, os
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

class StripeService:
    def create_checkout(self, price_id: str):
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            mode="subscription",
            line_items=[{"price": price_id, "quantity": 1}],
            success_url="/success",
            cancel_url="/cancel"
        )
        return session.url

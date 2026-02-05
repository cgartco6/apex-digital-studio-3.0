import hashlib, urllib.parse, os

class PayFastService:
    def generate_payment_url(self, data: dict):
        query = urllib.parse.urlencode(data)
        signature = hashlib.md5(query.encode()).hexdigest()
        return f"https://sandbox.payfast.co.za/eng/process?{query}&signature={signature}"

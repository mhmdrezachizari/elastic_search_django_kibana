# services.py

from datetime import timedelta
from django.utils import timezone
from .models import OTP


def create_otp(phone: str):
    code = OTP.generate_code()

    otp = OTP.objects.create(
        phone=phone,
        code=code,
        expires_at=timezone.now() + timedelta(minutes=2)
    )

    print(f"OTP for {phone}: {code}")

    return otp
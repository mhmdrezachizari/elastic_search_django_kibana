# models.py

from django.db import models
from django.utils import timezone
import random


class OTP(models.Model):
    phone = models.CharField(max_length=15, db_index=True)
    code = models.CharField(max_length=6)

    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def is_valid(self):
        return (
            not self.is_used
            and self.expires_at > timezone.now()
        )

    @staticmethod
    def generate_code():
        return str(random.randint(100000, 999999))
# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import OTP
from .services import create_otp


class SendOTPView(APIView):

    def post(self, request):
        phone = request.data.get("phone")

        if not phone:
            return Response(
                {"error": "phone is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        create_otp(phone)

        return Response({
            "message": "OTP sent successfully"
        })


from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .models import OTP

User = get_user_model()


class VerifyOTPView(APIView):

    def post(self, request):
        phone = request.data.get("phone")
        code = request.data.get("code")

        otp = OTP.objects.filter(
            phone=phone,
            code=code,
            is_used=False
        ).order_by("-created_at").first()

        if not otp or not otp.is_valid():
            return Response(
                {"error": "Invalid or expired code"},
                status=400
            )

        otp.is_used = True
        otp.save()

        user, created = User.objects.get_or_create(
            username=phone,
            defaults={"username": phone}
        )

        refresh = RefreshToken.for_user(user)

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        })
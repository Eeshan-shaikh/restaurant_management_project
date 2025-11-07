from django.shortcuts import render

# Create your views here.
from rest_framework.view import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Coupon

class CouponValidationView(APIiew):
    def post(self, request):
        code = request.data.get("code", '').strip()
        if not code:
            return Response({"error": "This coupon is not active"}, status = status.HTTP_400_BAD_REQUEST)

        try:
            coupon = coupon.object.get(code_iexact=code)
        except coupon.DoesNotExist:
            return Response({"error": "Invalid coupon code"}, status=status.HTTP_400_BAD_REQUEST)

        today = timezone.now().date()

        if not coupon.is_active:
            return Response({"error":"This coupon is not active"}, status=status.HTTP_400_BAD_REQUEST)

        if not(coupon.valid_from <= today <= coupon.valid_until):
            return Response({"error":"this coupon is not valid at this time"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "success": True,
            "code": coupon.code,
            "discount_percentage" : coupon.discount_percentage
        }, status=status.HTTP_200_OK)
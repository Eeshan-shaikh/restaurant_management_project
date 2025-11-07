from django.urls import path
from .views import *

urlpatterns = [
    path("coupons/validate/", couponValidationview.as_view(), name="coupon-validate"),
]
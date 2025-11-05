from rest_framework import serializers
from .models import Menucategory

class MenucategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Menucategory
        field = ["id", "name"]
        
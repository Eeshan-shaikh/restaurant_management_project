from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from .model import MenuCategory
from .serializers import MenuCategorySerializer

class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.object.all()
    serializer_class = MenuCategorySerializer
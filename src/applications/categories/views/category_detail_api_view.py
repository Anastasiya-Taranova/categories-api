from rest_framework import generics

from applications.categories.models import Category
from applications.categories.serializers.category_serializer import \
    CategorySerializer


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

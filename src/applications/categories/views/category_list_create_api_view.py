from rest_framework import generics, status
from rest_framework.response import Response

from applications.categories.models import Category
from applications.categories.serializers.category_serializer import \
    CategorySerializer


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        Category.dump_data(request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

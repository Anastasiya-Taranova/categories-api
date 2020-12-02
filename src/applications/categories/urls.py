from django.urls import path

from applications.categories.views.category_detail_api_view import CategoryDetailAPIView
from applications.categories.views.category_list_create_api_view import CategoryListCreateAPIView

urlpatterns = [
    path('', CategoryListCreateAPIView.as_view()),
    path('<int:pk>/', CategoryDetailAPIView.as_view()),
]

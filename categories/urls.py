from django.urls import path
from .views import CategoryList, CategoryCreate

urlpatterns = [
    path('category/', CategoryList.as_view(), name='category'),
    path('category/new', CategoryCreate.as_view(), name='create_category'),
]
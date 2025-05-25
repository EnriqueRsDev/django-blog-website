from django.urls import path
from .views import PostList, PostCreate

urlpatterns = [
    path('post/', PostList.as_view(), name='post_list'),  # Lista de posts
    path('post/new', PostCreate.as_view(), name='new-post'),  # Detalle post
]
from django.urls import path
from .views import PostList, PostCreate, PostDetails, MyPosts, PostEdit, PostDelete

urlpatterns = [
    path('', PostList.as_view(), name='posts'),
    path('myposts/', MyPosts.as_view(), name='my-posts'),
    path('new/', PostCreate.as_view(), name='new-post'),
    path('<slug:slug>/edit/', PostEdit.as_view(), name='edit-post'),
    path('<slug:slug>/delete/', PostDelete.as_view(), name='delete-post'),
    path('<slug:slug>/', PostDetails.as_view(), name='post-detail')
]
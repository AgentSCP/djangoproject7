from .views import GetPosts, GetDetail, CreatePost, UpdatePost, DeletePost, index
from django.urls import path

urlpatterns = [
    path('', GetPosts.as_view(), name='home'),
    path('detail/<int:ph>', GetDetail.as_view(), name='detail'),
    path('create/', CreatePost.as_view(), name='create'),
    path('update/<int:ph>', UpdatePost.as_view, name='update'),
    path('delete/<int:ph>', DeletePost.as_view, name='delete'),
    path('test', index)
]
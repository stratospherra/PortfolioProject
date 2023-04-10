from django.urls import path
from .views import AddPostView, PostListView

urlpatterns = [
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('post_list/', PostListView.as_view(), name='post_list' )
]

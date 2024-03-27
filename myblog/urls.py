from django.urls import path

from .views import *

urlpatterns = [
  path("", IndexView.as_view(), name="index"),
  path("add_post/", CreatePostView.as_view(), name="create_post"),
  path("add_category/", AddCategoryView.as_view(), name="add_category"),
  path("post/<int:pk>/", PostView.as_view(), name="post"),
  path("post/<int:pk>/edit_post/", UpdatePostView.as_view(), name="update_post"),
  path("post/<int:pk>/delete_post/", DeletePostView.as_view(), name="delete_post"),
]

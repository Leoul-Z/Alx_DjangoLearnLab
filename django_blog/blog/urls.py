from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView
)
from .views import add_comment, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path("posts/", PostListView.as_view(), name="post-list"),
    path("post/new/", PostCreateView.as_view(),
         name="post-create"),          # <-- added
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(),
         name="post-update"),  # <-- added
    path("post/<int:pk>/delete/", PostDeleteView.as_view(),
         name="post-delete"),  # <-- added
    path("post/<int:post_id>/comments/new/", add_comment, name="add-comment"),
    path("comments/<int:pk>/update/",
         CommentUpdateView.as_view(), name="comment-update"),
    path("comments/<int:pk>/delete/",
         CommentDeleteView.as_view(), name="comment-delete"),
]

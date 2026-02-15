from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView,
    CommentCreateView, CommentUpdateView, CommentDeleteView
)
from .views import SearchResultsView, PostListView

urlpatterns = [
    # Post CRUD
    path("posts/", PostListView.as_view(), name="post-list"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),

    # Comment CRUD
    path("post/<int:post_id>/comments/new/",
         CommentCreateView.as_view(), name="comment-create"),   # create
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(),
         name="comment-update"),           # update
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(),
         name="comment-delete"),           # delete
    path("search/", SearchResultsView.as_view(), name="search-results"),
    path("tags/<str:tag_name>/", PostListView.as_view(), name="posts-by-tag"),
]

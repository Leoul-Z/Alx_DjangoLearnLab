from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),

    # Posts
    path('', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comments
    path('posts/<int:post_id>/comment/', add_comment, name='comment-create'),
    path('comments/<int:comment_id>/edit/',
         edit_comment, name='comment-update'),
    path('comments/<int:comment_id>/delete/',
         delete_comment, name='comment-delete'),
]

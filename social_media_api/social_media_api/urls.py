from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    # this line must point to posts/urls.py
    path('api/', include('posts.urls')),
]

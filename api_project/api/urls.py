from django.contrib import admin
from django.urls import path, include   # include is needed

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ Add this line to include your api app’s URLs
    path('api/', include('api.urls')),
]

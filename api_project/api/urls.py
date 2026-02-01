from django.urls import path
from .views import BookList   # import the view

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

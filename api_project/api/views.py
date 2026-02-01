from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Simple list view (already added earlier)


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Full CRUD ViewSet


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

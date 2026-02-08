from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework as django_filters  # ✅ Correct import
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    List all books with filtering, searching, and ordering.
    - Filtering: by title, author name, publication_year
    - Searching: text search on title and author name
    - Ordering: by title or publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Filtering, searching, ordering backends
    filter_backends = [django_filters.DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    # Filtering
    filterset_fields = ["title", "author__name", "publication_year"]

    # Searching
    search_fields = ["title", "author__name"]

    # Ordering
    ordering_fields = ["title", "publication_year"]
    ordering = ["title"]  # default ordering

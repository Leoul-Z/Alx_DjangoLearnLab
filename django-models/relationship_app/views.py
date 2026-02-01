from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library


# ------------------------------
# Function-based View (FBV)
# ------------------------------
def list_books(request):
    """
    Displays a list of all books in the database.
    """
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})


# ------------------------------
# Class-based View (CBV)
# ------------------------------
class LibraryDetailView(DetailView):
    """
    Displays details of a single library, including all books in that library.
    """
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

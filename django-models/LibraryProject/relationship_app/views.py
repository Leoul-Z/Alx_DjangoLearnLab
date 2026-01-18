from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view: simple text output


def list_books(request):
    books = Book.objects.all()
    output = []
    for book in books:
        output.append(f"{book.title} by {book.author.name}")
    return HttpResponse("\n".join(output))


# Class-based view using DetailView
class LibraryDetailView(DetailView):
    model = Library

    def get(self, request, *args, **kwargs):
        library = self.get_object()
        books = library.books.all()
        output = [f"Library: {library.name}", "Books:"]
        for book in books:
            output.append(f"{book.title} by {book.author.name}")
        return HttpResponse("\n".join(output))

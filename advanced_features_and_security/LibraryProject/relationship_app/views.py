from django.http import HttpResponse
from django.views.generic import DetailView
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Book, Library


# ---- Task 1 ----

def list_books(request):
    books = Book.objects.all()
    output = []
    for book in books:
        output.append(f"{book.title} by {book.author.name}")
    return HttpResponse("\n".join(output))


class LibraryDetailView(DetailView):
    model = Library

    def get(self, request, *args, **kwargs):
        library = self.get_object()
        books = library.books.all()
        output = [f"Library: {library.name}", "Books:"]
        for book in books:
            output.append(f"{book.title} by {book.author.name}")
        return HttpResponse("\n".join(output))


# ---- Task 2 ----

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# ---- Task 3 ----

def is_admin(user):
    return user.userprofile.role == 'Admin'


def is_librarian(user):
    return user.userprofile.role == 'Librarian'


def is_member(user):
    return user.userprofile.role == 'Member'


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# ---- Task 4 ----

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    return HttpResponse("Add book page")


@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    return HttpResponse("Edit book page")


@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    return HttpResponse("Delete book page")

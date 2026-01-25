from django.http import HttpResponse
from django.views.generic import DetailView
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .models import Book, Library


# ---- Task 1: List Books & Library Detail ----
@permission_required('bookshelf.can_view', raise_exception=True)
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


# ---- Task 2: User Registration ----
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Assign default group (Members)
            member_group, _ = Group.objects.get_or_create(name="Members")
            user.groups.add(member_group)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# ---- Task 3: Role-Based Views ----
def is_admin(user):
    return user.groups.filter(name="Admins").exists()


def is_librarian(user):
    return user.groups.filter(name="Librarians").exists()


def is_member(user):
    return user.groups.filter(name="Members").exists()


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# ---- Task 4: Permission-Protected Views ----
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    return HttpResponse("Add book page")


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    return HttpResponse("Edit book page")


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    return HttpResponse("Delete book page")

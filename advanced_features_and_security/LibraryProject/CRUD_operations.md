# CRUD Operations in Django Shell

This document records the **Create, Retrieve, Update, and Delete (CRUD)** operations
performed on the `Book` model in the `bookshelf` app using the Django shell.

---

## 1. Create Operation

**Command:**
```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book


Output:
<Book: 1984 by George Orwell>

### 2.Retrieve Operation
**Command:**
```python

Book.objects.all()


Output:

<QuerySet [<Book: 1984 by George Orwell>]>

## Update Operation

Command:

book.title = "Nineteen Eighty-Four"
book.save()
book


Output:

<Book: Nineteen Eighty-Four by George Orwell>

## Delete Operation

***Command:***

book.delete()
Book.objects.all()


Output:

<QuerySet []>
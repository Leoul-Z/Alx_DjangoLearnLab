# Delete Operation

This file documents how to delete a `Book` object from the database using Django ORM.

---

## Delete a Book

```python
from bookshelf.models import Book

# First, retrieve the book you want to delete
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion
Book.objects.all()

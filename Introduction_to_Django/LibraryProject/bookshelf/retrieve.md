# Retrieve Operation

This file documents how to retrieve `Book` objects from the database using Django ORM.

---

## Retrieve All Books

```python
from bookshelf.models import Book
Book.objects.all()
Book.objects.get(title="1984")

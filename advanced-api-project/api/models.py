from django.db import models

# Create your models here.
from django.db import models

# Author model represents a writer who can have multiple books.
# This establishes the "one" side of a one-to-many relationship.


class Author(models.Model):
    # Stores the author's name
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Book model represents individual books written by an Author.
# Each Book is linked to exactly one Author using ForeignKey.
class Book(models.Model):
    # Book title
    title = models.CharField(max_length=200)

    # Year book was published
    publication_year = models.IntegerField()

    # ForeignKey establishes one Author → many Books relationship
    author = models.ForeignKey(
        Author,
        related_name='books',  # allows accessing books via author.books.all()
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

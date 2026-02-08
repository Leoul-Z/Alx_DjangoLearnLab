from rest_framework import serializers
from .models import Author, Book
import datetime

# Serializes Book model including all fields.
# Also includes validation to ensure publication_year is not in the future.


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation
    def validate_publication_year(self, value):
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future.")
        return value


# Serializes Author model.
# Includes nested BookSerializer to show all books written by the author.
class AuthorSerializer(serializers.ModelSerializer):

    # Nested serializer shows related books dynamically.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

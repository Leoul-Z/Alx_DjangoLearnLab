from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username="testuser", password="password123")

        # Create test author and book
        self.author = Author.objects.create(name="George Orwell")
        self.book1 = Book.objects.create(
            title="1984", publication_year=1949, author=self.author)
        self.book2 = Book.objects.create(
            title="Animal Farm", publication_year=1945, author=self.author)

        # Authenticated client
        self.client_auth = APIClient()
        self.client_auth.login(username="testuser", password="password123")

    # ---------- CRUD TESTS ----------

    def test_list_books(self):
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_retrieve_book(self):
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "1984")

    def test_create_book_authenticated(self):
        url = reverse("book-create")
        data = {"title": "Homage to Catalonia",
                "publication_year": 1938, "author": self.author.id}
        response = self.client_auth.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        url = reverse("book-create")
        data = {"title": "Coming Up for Air",
                "publication_year": 1939, "author": self.author.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        url = reverse("book-update", args=[self.book1.id])
        data = {"title": "Nineteen Eighty-Four",
                "publication_year": 1949, "author": self.author.id}
        response = self.client_auth.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Nineteen Eighty-Four")

    def test_delete_book_authenticated(self):
        url = reverse("book-delete", args=[self.book2.id])
        response = self.client_auth.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_delete_book_unauthenticated(self):
        url = reverse("book-delete", args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ---------- FILTERING, SEARCHING, ORDERING ----------

    def test_filter_books_by_year(self):
        url = reverse("book-list") + "?publication_year=1949"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "1984")

    def test_search_books(self):
        url = reverse("book-list") + "?search=Animal"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(
            any("Animal Farm" in b["title"] for b in response.data))

    def test_order_books_by_year_desc(self):
        url = reverse("book-list") + "?ordering=-publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [b["publication_year"] for b in response.data]
        self.assertEqual(years, sorted(years, reverse=True))

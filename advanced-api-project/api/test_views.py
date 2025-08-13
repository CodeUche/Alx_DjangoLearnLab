from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from api.models import Book, Author


# Create your tests here
class ListViewTest(APITestCase):
    def setUp(self):  # This method is called before each test
        self.client = APIClient()  # Create a new client
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )  # Create a new user
        self.client.force_authenticate(user=self.user)  # Authenticate the client
        # Create some test data
        self.author1 = Author.objects.create(name="Jane Austen")
        self.author2 = Author.objects.create(name="John Locke")

        # Create some books
        self.book1 = Book.objects.create(
            title="Pride and Prejudice", author=self.author1, publication_year=1813
        )
        self.book2 = Book.objects.create(
            title="Laws of Attraction", author=self.author2, publication_year=2005
        )

    # Test the list view

    def test_list_view(self):
        url = reverse("book-list")  # Get the URL
        response = self.client.get(url)  # Send a GET request
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )  # Check the status code
        self.assertEqual(len(response.data), 2)

    # Test the create view
    def test_create_book(self):
        url = reverse("book-list")
        data = {
            "title": "New Book",
            "author": self.author1.id,
            "publication_year": 2024,
        }  # Send a POST request
        # Create a new book
        response = self.client.post(url, data)  # Send a POST request
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )  # Check the status code
        self.assertEqual(Book.objects.count(), 3)  # Check the number of books

    # Test the retrieve view
    def test_retrieve_book(self):
        url = reverse("book-detail", args=[self.book2.id])  # Get the URL
        response = self.client.get(url)  # Send a GET request
        # Check the status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Laws of Attraction")

    # Test the update view
    def test_update_book(self):
        url = reverse("book-detail", args=[self.book1.id])  # Get the URL
        data = {
            "title": "Updated Title",
            "author": self.author1.id,
            "publication_year": 2000,
        }  # Send a PUT request
        # Update the book
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    # Test the delete view
    # Delete the book
    def test_delete_book(self):
        url = reverse("book-detail", args=[self.book2.id])  #  Get the URL
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())

    # Test the search view
    # Search for a book
    def test_search_books(self):
        response = self.client.get("/books/?search=Attraction")  # Send a GET request
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Check the number of books
        self.assertEqual(
            response.data[0]["title"], "Laws of Attraction"
        )  # Check the title

    # Test the filter view
    # Filter books by author
    def test_filter_books_by_author(self):
        response = self.client.get(
            f"/books/?author={self.author1.id}"
        )  #   Send a GET request

        # Check the status code
        # Check the number of books
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], self.author1.id)

    def test_unauthenticated_create_book(self):
        self.client.logout()
        url = reverse("book-list")
        data = {
            "title": "Unauthorized Book",
            "author": self.author1.id,
            "publication_year": 2024,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthenticated_update_book(self):
        self.client.logout()
        url = reverse("book-detail", args=[self.book1.id])
        data = {
            "title": "Unauthorized Update",
            "author": self.author1.id,
            "publication_year": 2024,
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthenticated_delete_book(self):
        self.client.logout()
        url = reverse("book-detail", args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_search_by_author_name(self):
        response = self.client.get("/books/?search=Austen")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
        self.assertIn("Austen", response.data[0]["author_name"])

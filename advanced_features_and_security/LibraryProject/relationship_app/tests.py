from django.test import TestCase
from relationship_app.models import Author, Book, Library, Librarian

# Create your tests here.

class RelationshipAppTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="John Doe", email="johndoe@example.com")
        self.book = Book.objects.create(title="Django for Beginners", author=self.author)
        self.library = Library.objects.create(name="City Library")
        self.library.books.add(self.book)
        self.librarian = Librarian.objects.create(name="Jane Smith", library=self.library)
    
    def test_author_creation(self):
        self.assertEqual(self.author.name, "John Doe")
        self.assertEqual(self.author.email, "johndoe@example.com")
from .models import Author, Book, Library, Librarian
from django.shortcuts import render
from bookshelf.models import Book
def sample_query(request):
    # Fetch all books by a specific author
    napoleon = Author.objects.get(author_name='Napoleon Hill')
    napoleon_books = Book.objects.filter(author=napoleon)

    # Fetch all books in a library

    library_name = "City Library"
    library = Library.objects.get(name=library_name)
    library_books = library.books.all()

    
    # Fetch all librarians
    librarians = Librarian.objects.get(library=library)
    
    print("Napoleon Hill's Books:", napoleon_books)
    print("Books in", library_name, ":", library_books)
    print("Librarians in", library_name, ":", librarians)
  
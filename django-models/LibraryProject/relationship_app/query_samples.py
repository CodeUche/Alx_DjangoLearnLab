from .models import Author, Book, Library, Librarian
from django.shortcuts import render

def book_list(request):
    authors = Author.objects.filter(name = 'Napoleon Hill')  # Fetch all authors
    books = Book.objects.all()  # Fetch all books
    library = Library.objects.first()  # Fetch the first library
    librarians = Librarian.objects.all()  # Fetch all librarians
    
    return render(request, 'relationship_app/book_list.html', {
        'books': books,
        'authors': authors,
        'library': library,
        'librarians': librarians
        })

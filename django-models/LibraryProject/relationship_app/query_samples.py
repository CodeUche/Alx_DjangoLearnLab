from .models import Author, Book, Library, Librarian
from django.shortcuts import render

library_name = Library.objects.create(name="City Library")
def book_list(request):
    authors = Author.objects.filter(name = 'Napoleon Hill')  # Fetch all authors
    books = Book.objects.all()  # Fetch all books
    library = Library.objects.get(name = library_name)  # Fetch the first library
    librarians = Librarian.objects.all()  # Fetch all librarians
    
    return render(request, 'relationship_app/book_list.html', {
        'books': books,
        'authors': authors,
        'library': library,
        'librarians': librarians
        })

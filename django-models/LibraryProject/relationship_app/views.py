from django.shortcuts import render
from relationship_app.models import Author, Book, Library, Librarian
from django.http import HttpResponse
from .models import Library
from django.views.generic.detail import DetailView

# Create your views here.
library_name = "City Library"
def list_books(request):
    authors = Author.objects.filter(name = 'Napoleon Hill')  # Fetch all authors
    books = Book.objects.all()  # Fetch all books
    library = Library.objects.get(name = library_name)  # Fetch the first library
    librarians = Librarian.objects.all()  # Fetch all librarians
    
    return render(request, 'relationship_app/list_books.html', {
        'books': books,
        'authors': authors,
        'library': library,
        'librarians': librarians
        })

# Create a class-based view that displays details of a specific library
class LibraryDetailView(DetailView):
    def get(self, request, library_id):
        try:
            library = Library.objects.get(id=library_id)
            books = library.books.all()
            return render(request, 'relationship_app/library_detail.html', {
                'library': library,
                'books': books
            })
        except Library.DoesNotExist:
            return HttpResponse("Library not found", status=404)

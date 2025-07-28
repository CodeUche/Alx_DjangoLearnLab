from django.shortcuts import render
from relationship_app.models import Author, Book, Library, Librarian
# Create your views here.
def index(request):
    relationships = {
        'authors': Author.objects.all(),
        'books': Book.objects.all(),
        'libraries': Library.objects.all(),
        'librarians': Librarian.objects.all(),
    }
    return render(request, 'relationship_app/index.html', relationships)
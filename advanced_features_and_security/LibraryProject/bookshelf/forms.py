from django.shortcuts import render
from .models import Book


def ExampleForm(request):
    query = request.GET.get("q")
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = []
    return render(request, "bookshelf/search.html", {"books": books})

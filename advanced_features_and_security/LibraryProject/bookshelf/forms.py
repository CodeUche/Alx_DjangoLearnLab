from django.shortcuts import render
from .models import Book
from django.utils.html import escape


# Secure Data Access
# Modify views to avoid SQL injection and ensure safe handling of user input,
# especially in search functionalities or where direct SQL queries are used
class ExampleForm:
    @staticmethod  # This decorator makes the method static
    def search_book(request):  # This method handles the search functionality
        query = request.GET.get("q")  # Get the search query

        if query:
            query = escape(query)  # This line prevents HTML injection
            books = Book.objects.filter(
                title__icontains=query
            )  # This line prevents SQL injection
        else:
            books = []  # Return an empty list if no query is provided
        return render(request, "bookshelf/search.html", {"books": books})

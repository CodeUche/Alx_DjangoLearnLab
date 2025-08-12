from django.contrib import admin
from .models import Book, Author

# Register your models here.

admin.site.register(Book)  # Register the Book model
admin.site.register(Author)  # Register the Author

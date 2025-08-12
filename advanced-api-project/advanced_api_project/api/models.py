from django.db import models

# Create your models here.


# Create a book serializer to handle the book model
# Add name and email field
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    # This returns a string representation of the Author object.
    # This allows you to print or display a concise representation of the author, showing its attributes.
    def __str__(self):
        return self.name


# Create a book serializer to handle the book model
# Add title, author and publication year fields and create a foreign key to set relationship to author model.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.PositiveIntegerField()

    # This returns a string representation of the Book object.
    # This allows you to print or display a concise representation of the book, showing its title.

    def __str__(self):
        return self.title

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Book, Author
from datetime import datetime


# Define a custom serializer for the Book model
# This serializer includes nested serializers for the Author: Firstname Lastname
class BookSerializer(serializers.ModelSerializer):

    # A nested BookSerializer is used to serialize the Author: Firstname Lastname
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    # Define the fields to be serialized
    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]

    # Add custom validation to ensure that the publication year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:  # Check if the publication year is in the future
            raise serializers.ValidationError(
                "Publication year cannot be in the future"
            )  # Raise a validation error
        return value  # Return the validated publication year


# Define a custom serializer for the Author model
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(
        many=True, read_only=True
    )  # A nested BookSerializer is used to serialize the Author: Firstname Lastname

    class Meta:
        model = Author
        fields = ["name"]

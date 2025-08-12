from rest_framework import serializers
from api.models import Author, Book


# Create a book serializer to handle the book model and validate publication year
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True, read_only=True)

    # Validate publicatin date cannot be a future year
    def validate_future_year(self, value):
        current_year = 2025  # This is the assigned current year
        if value > current_year:  # If publication year is greater than current year
            raise serializers.ValidationError(
                "Year cannot be a future date"
            )  # Raise error
        return value  # Return publication year

    class Meta:
        model = Book  # Set model
        fields = "__all__"  # Set fields


# Create a author serializer to handle the author model
class AuthorSerializer(serializers.ModelSerializer):  # Create a author serializer
    class Meta:
        model = Author  # Set model
        fields = ["id", "name"]  # Set fields

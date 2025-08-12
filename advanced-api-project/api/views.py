from rest_framework import generics, permissions
from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book

# Create your views here.


# A list view retrieving all querysets
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Customize to ensure they handle form submissions and data validation
    def perform_create(self, serializer):
        serializer.save()


# Book detail view to retrieve a single book by ID
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# A create view for adding a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# An update view for modifying an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Customize to ensure they handle form submissions and data validation
    def perform_update(self, serializer):
        serializer.save()


# A delete view for deleting a book
class BookDelete(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

from django.shortcuts import render
from rest_framework import generics 
from .serializers import BookSerializer
from .models import Book

# Create your views here.

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

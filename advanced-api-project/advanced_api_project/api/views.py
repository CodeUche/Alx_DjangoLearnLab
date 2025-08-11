from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def books(request):
    return render(request, "books.html")


def authors(request):
    return render(request, "authors.html")

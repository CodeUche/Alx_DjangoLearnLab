from django.shortcuts import render
from relationship_app.models import Author, Book, Library, Librarian
from django.http import HttpResponse
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# Create your views here.
library_name = "City Library"
def list_books(request):
    authors = Author.objects.filter(name = 'Napoleon Hill')  # Fetch all authors
    books = Book.objects.all()  # Fetch all books
    library = Library.objects.get(name = library_name)  # Fetch the first library
    librarians = Librarian.objects.all()  # Fetch all librarians
    
    return render(request, 'relationship_app/list_books.html', {
        'books': books,
        'authors': authors,
        'library': library,
        'librarians': librarians
        })

# Create a class-based view that displays details of a specific library
class LibraryDetailView(DetailView):
    def get(self, request, library_id):
        try:
            library = Library.objects.get(id=library_id)
            books = library.books.all()
            return render(request, 'relationship_app/library_detail.html', {
                'library': library,
                'books': books
            })
        except Library.DoesNotExist:
            return HttpResponse("Library not found", status=404)

# Create a view for user signup
def register(request):
    if request.method == 'POST': # Check if the request method is POST
        # Create a user creation form instance with the submitted data
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') # Get the username from the form
            password = form.cleaned_data.get('password1') # Get the password from the form
            user = authenticate(username=username, password=password) # Authenticate the user
            login(request, user)
            return redirect('home') # Redirect to a home page or another page after signup
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Create a view for user login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('http://127.0.0.1:8000/')
    else:
        form = AuthenticationForm() # Create an empty form for GET requests
    return render(request, 'relationship_app/login.html', {'form': form}) # Render the login form

# Create a view for user logout
def user_logout(request): # Logout the user
        logout(request) # Redirect to the login page after logout
        return redirect('login') # Redirect to the login page after logout
    
@login_required
def home(request):
    if request.user.is_authenticated:
        return HttpResponse(f"Welcome {request.user.name} to the Library Home Page!") # A simple home page response
    return HttpResponse("Welcome, guest! Please log in! ") # If the user is not authenticated, return this response.

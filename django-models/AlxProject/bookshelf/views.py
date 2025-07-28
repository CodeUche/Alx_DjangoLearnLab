from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def book_inventory(request):
    return HttpResponse("Welcome to the Bookshelf!")
context = {'book_inventory': Book.objects.all()}

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# This view allows users to create a new account using the UserCreationForm.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html' # Template for user signup

@login_required
def profile_view(request):
    # This view is protected and requires the user to be logged in.
    # It displays the user's profile information.
    return render(request, 'accounts/profile.html', {'user': request.user})

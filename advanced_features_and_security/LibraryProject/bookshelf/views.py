from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
def book_inventory(request):
    return HttpResponse("Welcome to the Bookshelf!")


context = {"book_inventory": Book.objects.all()}


def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})


# This view allows users to create a new account using the UserCreationForm.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"  # Template for user signup


@login_required
def profile_view(request):
    # This view is protected and requires the user to be logged in.
    # It displays the user's profile information.
    return render(request, "accounts/profile.html", {"user": request.user})


"""
Modify your views to check for these permissions before allowing users to perform certain actions.
Use decorators such as permission_required to enforce these permissions in your views.

Views to Modify or Create:
Ensure views that create, edit, or delete model instances check for the correct permissions.
Example: Use @permission_required('app_name.can_edit', raise_exception=True) to protect an edit view.
"""


# Modify your views to check for these permissions
@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, id):
    return HttpResponse("You have permission to edit a book!")


@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, id):
    return HttpResponse("You have permission to delete a book!")

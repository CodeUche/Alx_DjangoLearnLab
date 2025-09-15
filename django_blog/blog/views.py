from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View, ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django import forms
from .forms import EditProfileForm, UpdateEmailForm
from .models import Post


# ----------------------
# Custom Registration Form
# ----------------------
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


# ----------------------
# Registration View
# ----------------------
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request, f"Welcome {user.username}! You have successfully registered."
            )
            return redirect("login")  # Redirect to login after successful registration
        else:
            messages.error(
                request, "Registration failed. Please correct the errors below."
            )
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


# ----------------------
# Login View
# ----------------------
class Login(LoginView):
    template_name = "login.html"

    def form_valid(self, form):
        """Add a success message on successful login."""
        messages.success(self.request, "You have successfully logged in!")
        return super().form_valid(form)


# ----------------------
# Logout View
# ----------------------
class Logout(LogoutView):
    template_name = "logout.html"

    def dispatch(self, request, *args, **kwargs):
        """Add a logout message."""
        messages.success(request, "You have successfully logged out.")
        return super().dispatch(request, *args, **kwargs)


# ----------------------
# Profile Edit View
# ----------------------
class EditProfileDetails(View):
    template_name = "profile.html"
    form_class = EditProfileForm

    def get(self, request):
        form = self.form_class(instance=request.user)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully.")
            return redirect("profile")
        messages.error(
            request, "There was an error updating your profile. Please try again."
        )
        return render(request, self.template_name, {"form": form})


# ----------------------
# Profile View
# ----------------------
@login_required
def profile_view(request):
    return render(request, "profile.html", {"user": request.user})


# ----------------------
# Update Email View
# ----------------------
@login_required
def update_email(request):
    if request.method == "POST":
        form = UpdateEmailForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your email has been updated successfully.")
            return redirect("profile")
        else:
            messages.error(
                request, "There was an error updating your email. Please try again."
            )
    else:
        form = UpdateEmailForm(instance=request.user)
    return render(request, "update_email.html", {"form": form})


class ListView(ListView):
    model = Post
    template_name = "blog-list.html"
    context_object_name = "blogposts"

    def list(request):
        blogposts = BlogPost.objects.all()
        return render(request, "book-list.html", {"books": books})


class DetailView(DetailView):
    model = Post
    template_name = "blogpost-detail.html"
    context_object_name = "blogpost-detail"

    def detail(request, pk):
        blogpost = BlogPost.objects.get(id=id)
        return render(request, "blogpost-detail.html", {"blogpost": blogpost})


class CreateView(CreateView):
    model = Post
    template_name = "blogpost-create.html"
    fields = ["title", "content", "author", "published_date"]

    def create(request):
        blogpost = BlogPost.objects.create(
            title=title, content=content, author=author, publised_date=published_date
        )
        return render(request, "blogpost-create.html", {"blogpost": blogpost})


class UpdateView(UpdateView):
    model = Post
    template_name = "blogpost-update.html"
    fields = ["title", "content", "author", "published_date"]

    def update(request, pk):
        blogpost = BlogPost.objects.get(id=id)
        return render(request, "blogpost-update.html", {"blogpost": blogpost})


class DeleteView(DeleteView):
    model = Post
    template_name = "blogpost-delete.html"

    def delete(request, pk):
        blogpost = BlogPost.objects.get(id=id)
        return render(request, "blogpost-delete.html", {"blogpost": blogpost})

 
# ensure only autenticated users can create a post
class 
    def create_post(request, *args, **kwargs):
        if not request.user.is_authenticated:
            message.error(request, "You must be logged in to create a post.")
            return redirect("login")
        return super().create_post(request, *args, **kwargs)

@LoginRequiredMixin
def 
        
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django import forms
from .forms import EditProfileForm, UpdateEmailForm


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

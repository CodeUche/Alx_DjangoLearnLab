from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
            form.save()
            return redirect("login")  # Redirect to login after successful registration
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


# ----------------------
# Login View
# ----------------------
class Login(LoginView):
    template_name = "login.html"


# ----------------------
# Logout View
# ----------------------
class Logout(LogoutView):
    template_name = "logout.html"


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
            return redirect("home")
        return render(request, self.template_name, {"form": form})



# Profile View
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
            return redirect("profile")
    else:
        form = UpdateEmailForm(instance=request.user)
    return render(request, "update_email.html", {"form": form})

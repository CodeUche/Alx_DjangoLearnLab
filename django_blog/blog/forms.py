from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Register (Username, email, password1, password2)
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# Edit Profile (Username, password1, password2, first name, last name)
class EditProfileForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "first_name", "last_name"]


# Update Email separately
class UpdateEmailForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["email"]

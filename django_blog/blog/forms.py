from django import forms
from django.contrib.auth.forms import UserCreationForm, ModelForm
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


# Develop form for the Post model using ModelForm for creatign and updatin a post
class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

    # Automatically set author based on the logged in user
    # Automatically set published_date to the current date
    # Ensure title and content fields are required
    def __init__(self, *args, **kwargs):
        # Accept request objects so we can set the author
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()

        if not cleaned_data.get("title"):
            raise forms.ValidationError("Title is required.")

        if not cleaned_data.get("content"):
            raise forms.ValidationError("Content is required.")

        return cleaned_data

    def save(Self, commit=True):
        instance - super().save(commit=False)
        if self.request and self.request.user.is_authenticated:
            instance.author = self.request.user
        instance.published_date = timezone.now()
        if commit:
            instance.save()
        return instance


class UpdatePostForm(ModelForm):

    class Meta:
        model = Post
        fields = ["title", "content"]

    # ensure the form validates data properly and includs fields for title, content and automatically set author based on the logged in user
    def __init__(self, *args, **kwargs):
        # Accept request objects so we can set the author
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()

        if not cleaned_data.get("title"):
            raise forms.ValidationError("Title is required.")

        if not cleaned_data.get("content"):
            raise forms.ValidationError("Content is required.")

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.request and self.request.user.is_authenticated:
            instance.author = self.request.user
        if commit:
            instance.save()
        return instance

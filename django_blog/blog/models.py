from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def validate_image_size(image):
    max_size = 1024 * 1024 * 2
    if image.size > max_size:
        raise ValidationError("Image size should not exceed 2MB.")
    else:
        return image


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    # profile photo should use pillow to resize
    profile_photo = models.ImageField(
        upload_to="profiles/", validators=[validate_image_size], null=True, blank=True
    )
    bio = models.TextField(default="Enter a bio", blank=False, null=False)

    def __str__(self):
        return self.author


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey("User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class EditProfileForm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alias_name = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True, blank=False, null=False)
    username = models.CharField(max_length=50, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

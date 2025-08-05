from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.PositiveIntegerField()

def __str__(self):
    return self.title

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username=None, password=None, **extra_fields):
        if not email:
            raise ValueError("This email field must be set")
        email = self.normalize_email(email)
        user = self.model(
            username=username, 
            email=email
            )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if not password:
            raise ValueError("Superusers must have a password")
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must be a staff")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must be have is_superuser=True")
        return self.create_user(email, username, password, **extra_fields)
       

# Create a custom user model enriched with fields like date of birth and profile picture
def validate_image_size(image):
    max_size_kb = 512   #512KB
    if image.size > max_size_kb * 1024:
        raise ValidationError(f'Image size should not exceed {max_size_kb}KB.')

class CustomUser(AbstractUser):
    profile_photo = models.ImageField(upload_to='profiles/',
        null= True,
        blank=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validate_image_size
            ],
        help_text='Upload a JPG, or PNG file.'
    )
    alias_name = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True, blank=False, null=False)
    username = models.CharField(max_length=50, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()
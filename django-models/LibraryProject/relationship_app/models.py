from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _  # Import translation utilities 


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    def __str__(self):
        return self.name
    
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('admin', _('Admin')),
        ('librarian', _('Librarian')),
        ('member', _('Member')),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='member')
    
    def __str__(self):
        return f'{self.user.username} - {self.role}'
    

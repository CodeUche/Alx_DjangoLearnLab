from django.db import models
from django.contrib.auth import get_user_model

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
    class Meta:
        permissions = (
            ('can_add_book', 'Can add book'),
            ('can_change_book', 'Can change book'),
            ('can_delete_book', 'Can delete book'),
        )
        # Adding verbose names for better readability in the admin interface
        verbose_name = ('Book')
        verbose_name_plural = ('Books')
    
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
    
ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('librarian', 'Librarian'),
        ('member', 'Member'),
    )

User = get_user_model()
class UserProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='member')
    
    def __str__(self):
        return f'{self.user.username} - {self.role}'
    
# Create and assign "Can publish post" permission
class PublishPost(models.Model):
    # Add other fields
    class Meta:
        permissions = [
            ("can_publish_post", "Can publish post"),
            ("can_delete_comment", "Can delete comment"),
        ]

from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):

        return self.title


class Blogpost(models.Model):
    title = models.CharField(max_length=100)
    comments = models.ManyToManyField("Comment", blank=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.CharField(max_length=500)
    author = models.OneToOneField(Blogpost, on_delete=models.CASCADE)
    published_date = models.DateField()
    text = models.TextField()

    def __str__(self):
        return self.comment


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

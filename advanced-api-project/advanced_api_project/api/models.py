from django.db import models

# Create your models here.


class Author(models.Model):

    # A one to many relatonship of name to Book models's author attribute
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("Author", related_name="books", on_delete=models.CASCADE)
    publication_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title

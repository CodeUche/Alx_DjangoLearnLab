from django.contrib import admin
from .models import Book, CustomUser


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('author', 'publication_year',)

admin.site.register(Book, BookAdmin)


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'alias_name')
    list_filter = ['username',]

admin.site.register(CustomUser, CustomUserAdmin)
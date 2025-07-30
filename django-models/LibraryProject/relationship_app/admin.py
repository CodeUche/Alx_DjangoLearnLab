from django.contrib import admin
from .models import Author, Book, Library, Librarian

# Register your models here.
class relationshipAppAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    list_filter = ['name',]

admin.site.register(Author, relationshipAppAdmin)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
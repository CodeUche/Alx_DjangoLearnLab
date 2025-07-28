from django.contrib import admin
from relationship_app.models import Author

# Register your models here.
class relationshipAppAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    list_filter = ['name',]

admin.site.register(Author, relationshipAppAdmin)
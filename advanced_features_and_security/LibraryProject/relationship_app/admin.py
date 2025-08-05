from django.contrib import admin
from .models import Author, Book, Library, Librarian, CustomUserModel
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

# Register your models here.
class relationshipAppAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    list_filter = ['name',]

admin.site.register(Author, relationshipAppAdmin)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)


def Setup_publishers_group():
    # Create or get the group
    publisher_group, created = Group.objects.get_or_create(name='Publishers')

    # Get permission
    content_type = ContentType.objects.get_for_model(Book)
    publish_permission = Permission.objects.get(
        codename = 'can_publish_book',
        content_type = content_type
    )

    # Assign permission to group
    publisher_group.permissions.add(publish_permission)
    print("Publishers group configured with publish permissions.")


class CustomModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'alias_name')
    list_filter = ['username',]

admin.site.register(CustomUserModel)





"""
User = get_user_model
def assign_user_to_group(username, group_name):
    try:
        user = User.objects.get(username=username)
        group, created = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)
        print(f"{username} added to '{group_name}' group.")

    except User.DoesNotExist:
        print(f"User '{username}' does not exist.")

assign_user_to_group("Louisa_xyz", "Publishers")
assign_user_to_group("Louisa_xyz", "Reader")
assign_user_to_group("Louisa_xyz", "Editors")


# Create or get group and assign permissions/privileges to them
def assign_group_permission(group_name, permission_codenames):
    group, created = Group.objects.get_or_create(name=group_name)

    for codename in permission_codenames:
        try:
            permission = Permission.objects.get(codename=codename)
            group.permission.add(permission)
            print(f"Permission '{codename}' added to group '{group_name}'.")
        except Permission.DoesNotExist:
            print(f"Permission with codename '{codename}' does not exist.")

"""

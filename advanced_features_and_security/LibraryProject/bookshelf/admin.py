from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Group, Permission


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    search_fields = ("title", "author")
    list_filter = (
        "author",
        "publication_year",
    )


admin.site.register(Book, BookAdmin)


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email")
    search_fields = ("username", "alias_name")
    list_filter = [
        "username",
    ]


admin.site.register(CustomUser, CustomUserAdmin)

# Create groups and assign privilege to each group

User = get_user_model()

# Create users
User.objects.create_user("Louisa_xyz", "louisa@example.com", "password123")
User.objects.create_user("Uche", "uche@example.com", "passwordxyz")


def assign_user_to_group(username, group_name):
    try:
        user = User.objects.get(username=username)
        group, created = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)
        print(f"{username} added to '{group_name}' group.")

    except User.DoesNotExist:
        print(f"User '{username}' does not exist.")


assign_user_to_group("Louisa_xyz", "Admins")
assign_user_to_group("Louisa_xyz", "Viewers")
assign_user_to_group("Louisa_xyz", "Editors")
assign_user_to_group("Uche", "Editors")
assign_user_to_group("Uche", "Viewers")


# Create or get group and assign permissions/privileges to them
def assign_group_permission(group_name, permission_codenames):
    group, created = Group.objects.get_or_create(name=group_name)

    for codename in permission_codenames:
        try:
            permission = Permission.objects.get(codename=codename)
            group.permissions.add(permission)
            print(f"Permission '{codename}' added to group '{group_name}'.")
        except Permission.DoesNotExist:
            print(f"Permission with codename '{codename}' does not exist.")


# Assign each group specific permissions
assign_group_permission("Editors", ["can_edit", "can_create"])
assign_group_permission("Viewers", ["can_view"])
assign_group_permission("Admins", ["can_view", "can_edit", "can_create", "can_delete"])

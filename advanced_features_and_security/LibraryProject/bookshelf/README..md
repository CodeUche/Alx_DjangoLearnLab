# Permissions for the book model are set within the Book model and the permissions set are:
` ["can_view"]    # This is viewing privilege/access`
`["can_create"]  # This is the book creation privilege`
`["can_edit"]    # This is the editing privilege`
`["can_delete"]  # This gives the user/group delete privileges`

# These permissions are defined within the Book model.

# [verbose_name] and [verbose_name_plural] are added for readability in the admin interface.

# The CustomUserManager(BaserUserManager) model was created to take email and password as login credentials instead of only username and password. This model inherits attributes from Django's in-built BaseUserManager class as it contains the attributes needed for this logic.

# CustomUser(AbstractUser) model is created to add extra fields to the User such as:
    
    profile_photo,
    alias_name,
    date_of_birth,
    email,
    username

# thus extending the already existing AbstractUser model.
# [validate_image_size(image)] function defines file type required and the maximum image size allowed to be uploaded (512KB).

# To assign users to groups, I created test users with the following credentials:
`("Louisa_xyz", "louisa@example.com", "password123"),`
`("Uche", "uche@example.com", "passwordxyz")`


# To assign the users to a group, I created a function to automate the process <assign_user_to_group(username, group_name)> 


`def assign_user_to_group(username, group_name):`
    `try:`
        `user = User.objects.get(username=username)`
        `group, created = Group.objects.get_or_create``(name=group_name)`
        `user.groups.add(group)`
        `print(f"{username} added to '{group_name}' group.")`

    `except User.DoesNotExist:`
        `print(f"User '{username}' does not exist.")`



# and passed the user and name of group i want to add them into as parameters and raised a <User.DoesNotExist> exception accompanied with an error message to notify if user does not exist.

# I assigned the test users to different groups, giving them several privileges.

`assign_user_to_group("Louisa_xyz", "Admins")`
`assign_user_to_group("Louisa_xyz", "Viewers")`
`assign_user_to_group("Louisa_xyz", "Editors")`
`assign_user_to_group("Uche", "Editors")`
`assign_user_to_group("Uche", "Viewers")`

# I assigned ["can_edit" and "can_create"] privileges to the <Editors group>,`can_view` privilege to the <Viewers group>

def assign_group_permission(group_name, permission_codenames):
    group, created = Group.objects.get_or_create(name=group_name)

    for codename in permission_codenames:
        try:
            permission = Permission.objects.get(codename=codename)
            group.permissions.add(permission)
            print(f"Permission '{codename}' added to group '{group_name}'.")
        except Permission.DoesNotExist:
            print(f"Permission with codename '{codename}' does not exist.")


# Assign the necessary permissions to each group to ensure they have appropriate access levels. For instance, the "Editors" group should be able to create and edit books, while "Viewers" should only have view access.

assign_group_permission(`Editors`, [`can_edit`, `can_create`])
assign_group_permission(`Viewers`, [`can_view`])
assign_group_permission(`Admins`, [`can_view`, `can_edit`, `can_create`, `can_delete`])


The Admins group is given all permissions: `can_view`, `can_create`, `can_edit`, `can_delete`.



# In `views.py`, the following views were created to ensure that users with the correct permissions can perform actions on books.


@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, id):
    return HttpResponse("You have permission to edit a book!")


@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, id):
    return HttpResponse("You have permission to delete a book!")



# This view was created to modify views to check for "can_edit" and "can_delete" permissions




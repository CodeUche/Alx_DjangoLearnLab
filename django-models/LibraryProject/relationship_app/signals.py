from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile
from django.contrib.auth.models import User
from django.db.models.signals import post_migrate
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from .models import Book
# Automatic Creation: Use Django signals to automatically create a UserProfile when a new user is registered.

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save() 


@receiver(post_migrate)
def create_custom_permissions(sender, **kwargs):
    content_type = ContentType.objects.get_for_model(Book)

    add_book, _ = Permission.objects.get_or_create(
        codename='can_add_book',
        name='Can add book',
        content_type=content_type
    )
    change_book, _ = Permission.objects.get_or_create(
        codename='can_change_book',
        name='Can change book',
        content_type=content_type
    )
    delete_book, _ = Permission.objects.get_or_create(
        codename='can_delete_book',
        name='Can delete book',
        content_type=content_type
    )

    admin_group, _ = Group.objects.get_or_create(name='Admin_Group')
    admin_group.permissions.set([add_book, change_book, delete_book])


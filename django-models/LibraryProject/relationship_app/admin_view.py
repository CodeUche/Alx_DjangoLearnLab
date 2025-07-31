from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile
def admin_view(user):
    if user.is_authenticated:
        try:
            if user.UserProfile.role == 'admin':
                return HttpResponse("Welcome to the admin view!")  # A simple admin view response
        except UserProfile.DoesNotExist:
            pass
        return HttpResponse("You are not authorized to view this page.")
        
@user_passes_test(lambda u: u.is_authenticated and u.profile.role == 'admin')
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'admin'

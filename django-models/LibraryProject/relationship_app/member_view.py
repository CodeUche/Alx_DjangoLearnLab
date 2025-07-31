from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile
def member_view(user):
    try:
        if user.is_authenticated and user.userprofile.role == 'member':
            return HttpResponse("Welcome to the member view!")  # A simple member view response
    except UserProfile.DoesNotExist:
        pass
    return HttpResponse("You are not authorized to view this page. Continue as guest!")  # If the user is not authenticated or not a member, return this response.

@user_passes_test(lambda u: u.is_authenticated and u.profile.role == 'member')
def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'member'

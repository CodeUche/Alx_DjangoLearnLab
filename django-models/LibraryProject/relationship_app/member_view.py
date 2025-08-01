from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile
@user_passes_test(lambda u: u.is_authenticated and u.userprofile.role == 'member')
def member_view(request):
    return HttpResponse("Welcome to the member dashboard!")  # This view can be used to restrict access to member-only pages.
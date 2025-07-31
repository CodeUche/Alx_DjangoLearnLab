from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
def admin_view(request):
    if request.user.is_authenticated and request.user.is_staff:
        return HttpResponse("Welcome to the admin view!")  # A simple admin view response
    return HttpResponse("You are not authorized to view this page.")  # If the user is not authenticated or not an admin, return this response.

@user_passes_test(lambda u: u.is_authenticated and u.is_staff)
def admin_dashboard(request):
    return render(request, 'relationship_app/admin_dashboard.html', {
        'user': request.user
    })
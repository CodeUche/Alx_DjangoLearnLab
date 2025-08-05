from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: u.is_authenticated and u.profile.role == 'admin')
def admin_view(request):
    return HttpResponse("Welcome to the admin dashboard!")  # This view can be used to restrict access to admin-only pages.
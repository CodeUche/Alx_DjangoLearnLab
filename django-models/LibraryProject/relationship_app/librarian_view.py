from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

@user_passes_test(lambda u: u.is_authenticated and u.userprofile.role == 'librarian')
def librarian_view(request):
    return HttpResponse("Welcome to the librarian dashboard!")  # This view can be used to restrict access to librarian-only pages.
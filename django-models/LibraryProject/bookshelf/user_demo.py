from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

"""
# Create a demo user for the bookshelf application
user = User.objects.create_user('johndoe123', 'johndoe@example.com', 'password123')

# Retrieve the user based on username
user = User.objects.get(username='johndoe123')
"""
"""
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

"""
"""
Edit relationship_app/urls.py to include URL patterns that route to the newly created views.
Make sure to link both the function-based and class-based views.
"""
from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # URL for the book list view
    path('books/', list_books, name='list_books'),

    # URL for the library detail view
    path('library/<int:library_id>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]
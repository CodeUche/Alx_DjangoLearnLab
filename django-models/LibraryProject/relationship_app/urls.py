"""
Edit relationship_app/urls.py to include URL patterns that route to the newly created views.
Make sure to link both the function-based and class-based views.
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view

urlpatterns = [
    # URL for the book list view
    path('books/', views.list_books, name='list_books'),

    # URL for the library detail view
    path('library/<int:library_id>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Login, logout, and registration URLs
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    
    # URLs for the admin, librarian, and member dashboards
    # These views are protected by user_passes_test decorators in their respective modules
    path('admin-dashboard/', admin_view, name='admin_view'),
    path('librarian-dashboard/', librarian_view, name='librarian_view'),
    path('member-dashboard/', member_view, name='member_view'),
    
    # URLs for user permissions
    path('add-book/', views.add_book, name='add_book'), # Add book view
    path('edit-book/<int:id>/', views.change_book, name='change_book'), # Change book view
    path('delete-book/<int:id>/', views.delete_book, name='delete_book'), # Delete book view
    
]

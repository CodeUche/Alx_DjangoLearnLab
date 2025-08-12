from contrib import admin
from django.urls import path
from . import views


# Configure URL patterns to connect to the views with specific endpoints
# Each view should have a unique path corresponding to its functions (e.g. book-list, book-detail, author-list, author-detail)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("books/", views.BookList.as_view(), name="book-list"),
    path("books/<int:pk>", views.BookDetail.as_view(), name="book-detail"),
    path("authors/", views.AuthorList.as_view(), name="author-list"),
    path("authors/<int:pk>", views.AuthorDetail.as_view(), name="author-detail"),
]

from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from . import views
from .views import (
    CreateView,
    DetailView,
    AuthorList,
    AuthorDetail,
    ListView,
    UpdateView,
    DeleteView,
)


# Configure URL patterns to connect to the views with specific endpoints
# Each view should have a unique path corresponding to its functions (e.g. book-list, book-detail, author-list, author-detail)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("books/", views.ListView.as_view(), name="book-list"),
    path("books/<int:pk>", views.Detail
    view.as_view(), name="book-detail"),
    path("authors/", views.AuthorList.as_view(), name="author-list"),
    path("authors/<int:pk>", views.AuthorDetail.as_view(), name="author-detail"),

    # Path for the API endpoint token
    path("api/token/", obtain_auth_token, name="api-token"),
]

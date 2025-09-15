from django.urls import path, include
from . import views

# create url paths for the HTML templates using django's path() and include function

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("profile/", EditProfileDetails.as_view(), name="profile"),
    path("/posts/", ListView.as_view(), name="blogposts-list"),
    path("posts/new/", CreateView.as_view(), name="blogposts-create"),
    path("posts/<int:pk>/", DetailView.as_view(), name="blogposts-detail"),
    path("posts/<int:pk>/edit/", UpdateView.as_view(), name="blogposts-update"),
    path("posts/<int:pk>/delete/", DeleteView.as_view(), name="blogposts-delete"),
]

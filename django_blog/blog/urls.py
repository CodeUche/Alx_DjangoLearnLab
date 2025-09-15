from django.urls import path, include
from . import views

# create url paths for the HTML templates using django's path() and include function

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("profile/", EditProfileDetails.as_view(), name="profile"),
    path("/post/", ListView.as_view(), name="blogposts-list"),
    path("post/new/", CreateView.as_view(), name="blogposts-create"),
    path("post/<int:pk>/", DetailView.as_view(), name="blogposts-detail"),
    path("post/<int:pk>/update/", UpdateView.as_view(), name="blogposts-update"),
    path("post/<int:pk>/delete/", DeleteView.as_view(), name="blogposts-delete"),
]

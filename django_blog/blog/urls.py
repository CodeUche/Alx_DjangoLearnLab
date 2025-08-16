from django.urls import path, include
from . import views
from .views import (
    Login,
    Logout,
    register,
    EditProfileDetails,
)

# create url paths for the HTML templates using django's path() and include function

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("profile/edit/", EditProfileDetails.as_view(), name="edit_profile"),
]

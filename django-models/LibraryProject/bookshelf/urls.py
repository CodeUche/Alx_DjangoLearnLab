from .views import SignUpView
from django.urls import path, include
from .views import book_inventory, book_list
from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [

    # Admin site URL
    path('admin/', admin.site.urls),

    # Home page URL
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # Home page

    # Include bookshelf app URLs
    path('', include('bookshelf.urls')), # Include bookshelf app URLs

    path('', book_inventory, name='book_inventory'),
    path('books/', book_list, name='book_list'),
    
    # Authentication Login/Logout views
    path("signup/", SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Password reset views
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), 
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), 
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), 
         name='password_reset_complete'),

    # Password change views
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
         name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
         name='password_change_done'),

]

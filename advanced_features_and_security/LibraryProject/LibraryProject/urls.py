"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from relationship_app import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),  # Include relationship app URLs
    path('', views.home, name='home'),  # Home page view
    path('', TemplateView.as_view(template_name='relationship_app/home.html'), name='home_template'),  # Static home template    
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', views.user_login, name='login'),  # User login view
    path('register/', views.register, name='register'),  # User registration view
    
]

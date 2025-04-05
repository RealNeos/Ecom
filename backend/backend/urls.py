"""
URL configuration for the backend project.

The `urlpatterns` list routes URLs to views. For more information, please see:
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

from django.contrib import admin  # Import the admin site
from django.urls import path, include  # Import the path function for URL routing
from signup.views import RegisterView  # Import the view for user registration
from login.views import LoginView
from dashboard.views import Dashboard  # Import the views for login and dashboard
from rest_framework_simplejwt.views import (  # Import JWT views for token management
    TokenObtainPairView,
    TokenRefreshView,
)

# Define the URL patterns for the project
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('api/dashboard/', include('dashboard.urls')),  # Include the dashboard app's URLs  # Dashboard view for authenticated users
    path('api/login/', LoginView.as_view(), name='login'),  # Login view for user authentication
    path('api/signup/', RegisterView.as_view(), name='signup'),  # Signup view for user registration
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtain JWT access and refresh tokens
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh JWT access token
    path('api/logout/', include('logout.urls')),  # Logout app URLs
]

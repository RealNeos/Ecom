from django.shortcuts import render  # For rendering templates (not used in this file)
from rest_framework import generics  # Provides generic views for common patterns
from rest_framework.permissions import AllowAny  # Allows unrestricted access to the view
from django.contrib.auth import get_user_model  # Dynamically retrieves the user model used by the project
from .serializers import RegisterSerializer  # Import the serializer for user registration

# Dynamically get the user model to support custom user models
User = get_user_model()

# Create your views here.

# View for user registration
class RegisterView(generics.CreateAPIView):
    """
    Handles user registration by creating a new user instance.
    Uses the RegisterSerializer to validate and serialize the input data.
    """
    queryset = User.objects.all()  # Queryset containing all user instances
    permission_classes = [AllowAny]  # Allow access to anyone (no authentication required)
    serializer_class = RegisterSerializer  # Specify the serializer class to handle registration data
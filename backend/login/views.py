# Import necessary modules and classes
from django.shortcuts import render  # For rendering templates (not used in this file)
from .serializers import LoginSerializer, UserSerializer  # Custom serializers for login and user data
from django.contrib.auth import authenticate  # For user authentication
from rest_framework_simplejwt.tokens import RefreshToken  # For generating JWT tokens
from rest_framework import generics  # For creating generic API views
from rest_framework.response import Response  # For sending HTTP responses
from django.http import HttpResponse  # For basic HTTP responses (not used in this file)
from rest_framework.views import APIView  # For creating custom API views
from rest_framework.permissions import IsAuthenticated  # For enforcing authentication on views
from django.shortcuts import redirect  # For redirecting users (not used in this file)

# Create your views here.

# LoginView handles user login and JWT token generation
class LoginView(generics.GenericAPIView):
    # Specify the serializer class to validate login data
    serializer_class = LoginSerializer

    # Handle POST requests for user login
    def post(self, request, *args, **kwargs):
        # Extract username and password from the request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Check if both username and password are provided
        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=400)

        # Authenticate the user using Django's built-in authentication system
        user = authenticate(username=username, password=password)

        if user is not None:
            # If authentication is successful, generate JWT tokens
            refresh = RefreshToken.for_user(user)  # Generate refresh and access tokens
            user_serializer = UserSerializer(user)  # Serialize user data
            return Response({
                'refresh': str(refresh),  # Return the refresh token
                'access': str(refresh.access_token),  # Return the access token
                'user': user_serializer.data  # Return serialized user data
            })
        else:
            # If authentication fails, return an error response
            return Response({'error': 'Invalid credentials'}, status=400)

# Dashboard view for authenticated users
class Dashboard(APIView):
    # Enforce authentication for this view
    permission_classes = [IsAuthenticated]

    # Handle GET requests to display the dashboard
    def get(self, request):
        user = request.user  # Get the authenticated user
        user_serializer = UserSerializer(user)  # Serialize user data
        return Response({'message': f'Welcome to the dashboard, {request.user.first_name}!'})

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer  # Import UserSerializer from the dashboard.serializers module

# Create your views here.
class Dashboard(APIView):
    # Handle GET requests to display the dashboard
    def get(self, request):
        # Extract the token from the query parameters
        token = request.query_params.get('token')

        if not token:
            return Response({'error': 'Token is required'}, status=400)

        # Authenticate the user using the token
        jwt_authenticator = JWTAuthentication()
        try:
            validated_token = jwt_authenticator.get_validated_token(token)
            user = jwt_authenticator.get_user(validated_token)
        except Exception as e:
            return Response({'error': 'Invalid or expired token'}, status=401)

        # If authentication is successful, return the dashboard response
        user_serializer = UserSerializer(user)  # Serialize user data
        return Response({'message': f'Welcome to the dashboard, {user.first_name}!'})
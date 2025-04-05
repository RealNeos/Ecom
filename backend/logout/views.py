from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can log out

    def post(self, request):
        try:
            # Extract the refresh token from the request data or query parameters
            refresh_token = request.data.get('refresh_token') or request.query_params.get('token')
            if not refresh_token:
                return Response({'error': 'Refresh token is required'}, status=400)

            # Blacklist the refresh token
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({'message': 'Successfully logged out'}, status=200)
        except ValidationError:
            return Response({'error': 'Invalid or already blacklisted token'}, status=400)
        except Exception as e:
            return Response({'error': 'An error occurred while logging out'}, status=500)

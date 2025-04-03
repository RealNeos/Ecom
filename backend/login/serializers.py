# Import necessary modules
from rest_framework import serializers  # Provides serializer classes for handling data validation and transformation
from django.contrib.auth import get_user_model  # Retrieves the user model used by the project

# Get the user model dynamically to support custom user models
User = get_user_model()

# Serializer for user data
class UserSerializer(serializers.ModelSerializer):
    """
    Serializes the User model to include specific fields such as id, username, email, first_name, and last_name.
    """
    class Meta:
        model = User  # Specify the model to serialize
        fields = ('id', 'username', 'email', 'first_name', 'last_name')  # Fields to include in the serialized output

# Serializer for login data
class LoginSerializer(serializers.Serializer):
    """
    Validates login data by ensuring both username and password are provided.
    """
    username = serializers.CharField(required=True)  # Username field (required)
    password = serializers.CharField(required=True)  # Password field (required)
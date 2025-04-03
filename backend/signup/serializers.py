from rest_framework import serializers  # Provides serializer classes for data validation and transformation
from django.contrib.auth import get_user_model  # Dynamically retrieves the user model used by the project

# Serializer for user registration
class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializes and validates user registration data, and creates a new user instance.
    """

    class Meta:
        model = get_user_model()  # Specify the user model to serialize
        fields = ('username', 'email', 'password', 'first_name', 'last_name')  # Fields to include in the serialized output

    def create(self, validated_data):
        """
        Creates a new user instance with the validated data.
        Ensures the password is hashed by using the `create_user` method of the user model.
        """
        user = get_user_model().objects.create_user(
            username=validated_data['username'],  # Set the username
            email=validated_data['email'],  # Set the email
            password=validated_data['password'],  # Set the password (hashed internally)
            first_name=validated_data['first_name'],  # Set the first name
            last_name=validated_data['last_name']  # Set the last name
        )
        return user  # Return the created user instance


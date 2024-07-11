from rest_framework import serializers
from .models import UserEmail

class UserEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEmail
        fields = ['email']

from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User

class UserSerializer(serializers.ModelSerializer):
  # password = serializers.SerializerMethodField()

  class Meta:
    model = User
    fields = ("username", "password", "email", "education", "score")
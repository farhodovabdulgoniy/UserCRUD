from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import UserSerializer
from rest_framework.response import Response
from .models import User
from django.contrib.auth.hashers import make_password

class UserCRUD(APIView):

  def get(self, request):
    users = User.objects.all()
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = UserSerializer(data = request.data, many = False)
    if serializer.is_valid():
      if serializer.validated_data['password']:
        serializer.validated_data["password"] = make_password(serializer.validated_data["password"])
      serializer.save()

    return Response(f"user {serializer.data['username']} successfully resgistered")

  def patch(self, request):
    serializer = UserSerializer(instance = request.user, data = request.data, partial = True)
    if serializer.is_valid():
      if serializer.validated_data['password']:
        serializer.validated_data["password"] = make_password(serializer.validated_data["password"])
      serializer.save()

    return Response(f"user {serializer.data['username']} successfully updated")

  def delete(self,request):
    User.objects.get(id = request.user.id).delete()
    return Response("user deleted")
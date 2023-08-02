from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import RegisterSerializer, LoginSerializer, UserSerializer


# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        password = serializer.validated_data["password"]
        hashed_password = make_password(password)
        serializer.save(password=hashed_password)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        login(request, user)
        tokens = serializer.validated_data["tokens"]
        user_data = UserSerializer(user).data

        response_data = {"tokens": tokens, "user": user_data}

        return Response(response_data)

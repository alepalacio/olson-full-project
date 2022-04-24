from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from core.settings import base
from users.models import User
from users.serializers import UserListSerializer, UserCreateSerializer, UserUpdateSerializer, UserChangePasswordSerializer, UserResetPasswordSerializer, UserLoginSerializer

# Create your views here.

class UserAPIView(APIView):
    def get(self, request):
        try:
            users = User.objects.all()
            serializer = UserListSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserSignUpAPIView(APIView):
    """
    User signup. Input example:
    {
        "username":"myusername",
        "email":"email@email.com",
        "password":"password"
    }
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            serializer = UserCreateSerializer(data = request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data = {
                'msg':'Successfully registered.',
                'data':serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        except:
            data = {
                'msg':'Bad request.',
                'error': serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            instance = get_object_or_404(User, pk=request.user.id)
            serializer = UserUpdateSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            data = {
                'msg':'Not found.'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        try:
            instance = get_object_or_404(User, pk=request.user.id)
            serializer = UserUpdateSerializer(
                instance, data = request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data = {
                'msg': 'Successfully updated.',
                'data': serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        except:
            data = {
                'msg':'Bad request.',
                'error': serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

class UserChangePasswordAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        try:
            instance = get_object_or_404(User, pk=request.user.id)
            serializer = UserChangePasswordSerializer(instance, data = request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data = {
                "msg":"Successfully password changed."
            }
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserResetPasswordAPIView(APIView):

    permission_classes = [permissions.AllowAny]
    
    def put(self, request):
        try: 
            instance = get_object_or_404(User, pk=request.user.id)
            data = {
                "email":instance.email
            }
            serializer = UserResetPasswordSerializer(instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            data = {
                "msg":"Successfully password reset. Check your email."
            }
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors)

class UserLoginAPIView(APIView):
    """
    User signup. Input example:
    {
        "email":"email@email.com",
        "password":"password"
    }
    """

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            serializer = UserLoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            email = serializer.data["email"]
            password = serializer.data["password"]
            user = authenticate(email=email, password=password)

            if not user:
                return Response({
                    "msg":"Invalid credentials. Try again."
                }, status=status.HTTP_400_BAD_REQUEST) 
            
            token, _ = Token.objects.get_or_create(user=user)
            print(token.key)
            return Response({
                "msg":"Successfully logged in.",
                "token":token.key
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                "msg":"Bad request",
            }, status=status.HTTP_400_BAD_REQUEST)
            
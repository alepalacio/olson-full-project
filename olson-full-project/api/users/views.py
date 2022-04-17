from distutils import errors
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from users.serializers import UserSerializer, UserUpdateSerializer

# Create your views here.

class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserSignUpAPIView(APIView):
    """
    User signup. Input example:
    {
        "username":"myusername",
        "email":"email@email.com",
        "password":"password"
    }
    """
    def post(self, request):
        try:
            serializer = UserSerializer(data = request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data = {
                'msg':'Successfully registered.',
                'data': serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        except:
            data = {
                'msg':'Bad request.',
                'error': serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIView(APIView):

    def get(self, request):
        try:
            instance = get_object_or_404(User, pk=request.user.id)
            serializer = UserSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            data = {
                'msg':'Not found.'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            instance = get_object_or_404(User, pk=pk)
            serializer = UserUpdateSerializer(
                instance, data = request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data = {
                'msg': 'Succesfully updated.',
                'data': serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        except:
            data = {
                'msg':'Bad request.',
                'error': serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
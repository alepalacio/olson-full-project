from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from users.serializers import UserListSerializer, UserCreateSerializer, UserUpdateSerializer, UserChangePasswordSerializer, UserResetPasswordSerializer

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

    # def get(self, request):
    #     try:
    #         instance = get_object_or_404(User, pk=request.user.id)
    #         serializer = UserUpdateSerializer(instance)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     except:
    #         data = {
    #             'msg':'Not found.'
    #         }
    #         return Response(data, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            instance = get_object_or_404(User, pk=pk)
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
    def put(self, request, pk):
        try:
            instance = get_object_or_404(User, pk=pk)
            serializer = UserChangePasswordSerializer(instance, data = request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response('OK', status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserResetPasswordAPIView(APIView):
    def put(self, request, pk):
        try: 
            instance = get_object_or_404(User, pk=pk)
            serializer = UserResetPasswordSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data = {
                "msg":"Successfully password reset. Check your email."
            }
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors)
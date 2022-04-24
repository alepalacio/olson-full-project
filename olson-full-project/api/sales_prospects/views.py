from django.shortcuts import render
from rest_framework import status
from rest_framework import views
from rest_framework.response import Response
from .models import SalesProspectProfile
from .serializers import SalesProspectSerializer

# Create your views here.

class SalesProspectProfileAPIView(views.APIView):

    def post(self, request):
        
        try:
            serializer = SalesProspectSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
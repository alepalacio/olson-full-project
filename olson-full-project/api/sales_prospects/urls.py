from django.urls import path
from . import views

urlpatterns = [
    path('', views.SalesProspectProfileAPIView.as_view(),), 
]

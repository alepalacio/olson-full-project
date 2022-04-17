from django.urls import path
from users import views

urlpatterns = [
    path('users/', views.UserAPIView.as_view(),),
    path('signup/', views.UserSignUpAPIView.as_view(), name='user_signup',),
    path('update/<int:pk>/', views.UserDetailAPIView.as_view(), name='user_detail',),
]

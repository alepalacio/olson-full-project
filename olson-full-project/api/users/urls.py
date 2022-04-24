from django.urls import path
from users import views

urlpatterns = [
    path('users/', views.UserAPIView.as_view(),),
    path('signup/', views.UserSignUpAPIView.as_view(), name='user_signup',),
    path('update/<int:pk>/', views.UserDetailAPIView.as_view(), name='user_detail',),
    path('change_password/<int:pk>/', views.UserChangePasswordAPIView.as_view(),),
    path('reset_password/<int:pk>/', views.UserResetPasswordAPIView.as_view(),),
]

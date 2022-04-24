from django.urls import path
from users import views

urlpatterns = [
    path('users/', views.UserAPIView.as_view(),),
    path('signup/', views.UserSignUpAPIView.as_view(), name='user_signup',),
    path('login/', views.UserLoginAPIView.as_view(), name='user_login',),
    path('update/', views.UserDetailAPIView.as_view(), name='user_detail',),
    path('change_password/', views.UserChangePasswordAPIView.as_view(),),
    path('reset_password/', views.UserResetPasswordAPIView.as_view(),),
]

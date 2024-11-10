from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/',views.LoginApi.as_view(), name='login'),
    path('logout/',views.LogoutView.as_view()),
    path('signup/', views.UserCreateView.as_view()),
    path('users/', views.UserListView.as_view()),
    path('api-token-auth/', obtain_auth_token),


]
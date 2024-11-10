from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('items/', views.ItemsListApiView.as_view() , name='items'),
]

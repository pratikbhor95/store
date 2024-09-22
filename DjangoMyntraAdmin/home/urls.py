from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.MessageListView.as_view(), name='message-list'),
    path('messages/create/', views.MessageCreateView.as_view(),
         name='message-create'),
    path('items/', views.ItemsListView.as_view(), name='Items-list'),
    path('items/create/', views.ItemsCreateView.as_view(), name='Items-create'),
    # path('rating/', views.RatingListView.as_view(), name='Rating-list'),
    # path('rating/create/', views.RatingCreateView.as_view(), name='Rating-create'),

]

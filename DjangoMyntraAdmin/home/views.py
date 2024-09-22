from django.shortcuts import render

# Create your views here.


from rest_framework import generics, permissions
from .models import Message, Items
from .serializers import MessageSerializer, ItemsSerializer

from rest_framework.response import Response


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']


class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    http_method_names = ['get']


class ItemsCreateView(generics.CreateAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']


class ItemsListView(generics.ListAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    http_method_names = ['get']

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = ItemsSerializer(queryset, many=True)
        return Response(serializer.data)


# class RatingCreateView(generics.CreateAPIView):
#     queryset = Rating.objects.all()
#     serializer_class = RatingSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     http_method_names = ['post']


# class RatingListView(generics.ListAPIView):
#     queryset = Rating.objects.all()
#     serializer_class = RatingSerializer
#     http_method_names = ['get']

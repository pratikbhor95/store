from rest_framework import viewsets
from .models import Items , Message
from .serializers import ItemsSerializer #, ImageSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics , mixins

class ItemsListApiView(generics.ListAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    permission_classes = [IsAuthenticated]

    # @action(detail=True,methods='GET')
    # def ItemImages(self, request, pk=None):
    #     serializer = ImageSerializer(data = request.data)
    #     return Response(serializer.data)

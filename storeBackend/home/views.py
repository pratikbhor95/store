from rest_framework import viewsets
from .models import Items , Message
from .serializers import ItemsSerializer #, ImageSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class ItemsViewset(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

    # @action(detail=True,methods='GET')
    # def ItemImages(self, request, pk=None):
    #     serializer = ImageSerializer(data = request.data)
    #     return Response(serializer.data)

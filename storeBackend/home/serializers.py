from rest_framework import serializers
from .models import Message, Items #, Image


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class ItemsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Items
        fields = [
            'id',
            'created_at',
            'company',
            'item_name',
            'item_description',
            'sku',
            'original_price',
            'current_price',
            'discount_percentage',
            'return_period',
            'image',
        ]


# class ItemsSerializer(serializers.ModelSerializer)


# class ImageSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Image
#         fields = "__all__"



# class RatingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Rating
#         fields = '__all__'

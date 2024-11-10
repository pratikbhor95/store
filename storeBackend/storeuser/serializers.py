from rest_framework import serializers
from django.contrib.auth.models import User
from datetime import datetime
# from stockuser.models import StockUserModel 

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'id',
            'username',
        'password',
        'email',
        'first_name',
        'last_name',
        'date_joined']
        # read_only_fields = ['companyName','companySymbol', 'currency']
        extra_kwargs = {
            'password': {'write_only': True},
            'email' : {'required':True},
            'first_name': {'required': False},
            'last_name': {'required': False},
            'date_joined':{'read_only':True},
        }
        def create(self, validated_data):
            user = User(
                username=validated_data['username'],
                email=validated_data['email'],
                first_name=validated_data.get('first_name', ''),
                last_name=validated_data.get('last_name', ''),
                date_joined=datetime.now()  # Set the current datetime
            )
            user.set_password(validated_data['password'])
            user.save()
            return user
        
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
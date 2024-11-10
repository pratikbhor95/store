from django.contrib.auth.models import User
from storeuser.serializers import UserCreateSerializer , UserListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework import generics , status



# class UserCreateView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserCreateSerializer
#     permission_classes = [AllowAny]

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        # Call the parent class's create method to create the user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  # Save the user object

        # Generate a token for the newly created user
        token, created = Token.objects.get_or_create(user=user)

        # Return the user data along with the token
        return Response({
            'user': serializer.data,
            'token': token.key  # Include the token
        }, status=status.HTTP_201_CREATED)

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]


    
class LoginApi(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    http_method_names = ['post']
    
    def post(self, request, format=None):
        # user = authenticate(username = request.query_params.get('username', None),password=request.query_params.get('password',None))
        # Use request.data to access POST data
        username = request.data.get('username')
        password = request.data.get('password')
        print(username , password)
        user = authenticate(username=username, password=password)
        
        
        if user is not None:
            # Authentication successful
            # Get or create a token for the user
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.id,
                'username': user.username,
                'email': user.email
            }, status=status.HTTP_200_OK)
        else:
            # Authentication failed
            return Response({
                'detail': 'Invalid credentials'
            }, status=status.HTTP_401_UNAUTHORIZED)
        

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Get the current token from the request header
        token = request.auth
        
        if token:
            token.delete()  # Delete the token, logging the user out
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        
        return Response({"detail": "Token not found."}, status=status.HTTP_400_BAD_REQUEST)
        
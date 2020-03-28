from django.http import HttpResponse
from .serializers import UserSerializer,AuthTokenSerializer
from .models import User
from rest_framework import generics
from django.db.models import Q
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import get_user_model

def IndexView(request):
    return HttpResponse("DTU-NET")

class CustomAuthToken(ObtainAuthToken):
    serializer_class=AuthTokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
        })

class SignupAPIView(generics.CreateAPIView):
    authentication_classes=[]
    permission_classes=[]
    serializer_class=UserSerializer
    def get_queryset(self):
        return get_user_model().objects.all()

class UserListAPIView(generics.ListAPIView):
    serializer_class=UserSerializer
    def get_queryset(self):
        return get_user_model().objects.all()

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=UserSerializer

    def get_queryset(self):
        return get_user_model().objects.all()

    def get_object(self):
        return get_user_model().objects.get(u_id=self.kwargs['u_id'])

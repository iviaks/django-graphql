from rest_framework import viewsets
from api.v1.serializers import UserSerializer
from django.contrib.auth.models import User


class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

from django.core import serializers
from .models import User,Activity
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer

# API for getting all Users details in json format called using get request


class Activity(GenericAPIView):
    serializer_class = UserSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        out = {"ok": True, "members":serializer.data}
        return Response(out, status=200)

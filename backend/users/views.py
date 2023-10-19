from django.shortcuts import render
from rest_framework import viewsets, views, permissions
from .serializers import TestKitSerializer, UserProfileSerializer , ProfileSerializer
from . import models

# Create your views here.
class TestKitViewSet(viewsets.ModelViewSet):
    serializer_class = TestKitSerializer
    queryset = models.TestKit.objects.all()


class CreateProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserProfileSerializer
    action_serializers = {
        "retrieve": ProfileSerializer,
        "dafault": UserProfileSerializer,
        "update": UserProfileSerializer,
    }
    queryset = models.User.objects.all()

    # def post(self, request):

    #     srlzr = self.serializer_class(data=request.data, context={"request": request})
    #     srlzr.is_valid(raise_exception=True)
    #     user = srlzr.create(srlzr.validated_data)

    #     response_data = serializers.UserSerializer(user, context={"request": request}).data

    #     return Response(response_data, status=201)
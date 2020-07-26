from rest_framework.views import APIView
from utils.response import APIResponse
from rest_framework.viewsets import ModelViewSet
from utils.myModelViewSet import MyModelViewSet
from . import models
from .serializers import UserModelSerializer, CarModelSerializer


class Test(MyModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserModelSerializer


class Car(MyModelViewSet):
    queryset = models.Car.objects.all()
    serializer_class = CarModelSerializer

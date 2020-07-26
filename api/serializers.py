from rest_framework.serializers import ModelSerializer
from . import models


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username', 'password', 'email', 'mobile']
        extra_kwargs = {

        }


class CarModelSerializer(ModelSerializer):
    class Meta:
        model = models.Car
        fields = ['name', 'brand', 'price']
        extra_kwargs = {

        }

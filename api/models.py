from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Base(models.Model):
    is_create = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        abstract = True


class User(AbstractUser, Base):
    mobile = models.CharField(max_length=11)
    gender = models.CharField(max_length=2)

    class Meta:
        db_table = 'api_user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Car(Base):
    name = models.CharField(max_length=32)
    brand = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'api_car'
        verbose_name = '汽车'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

from . import views
from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('test', views.Test)
router.register('car', views.Car)
urlpatterns = [
    re_path(r'^', include(router.urls))
]

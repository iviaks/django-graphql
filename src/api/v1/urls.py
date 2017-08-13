from django.conf.urls import url, include
from api.v1.views import UserViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', UserViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
]

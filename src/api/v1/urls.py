from django.conf.urls import url
from api.v1.views import django_rest_view

urlpatterns = [
    url(r'^$', django_rest_view, name='home'),
]

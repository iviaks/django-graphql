from django.conf.urls import url
from api.v2.views import django_graphql

urlpatterns = [
    url(r'^$', django_graphql, name='home'),
]

from django.conf.urls import url
from apps.comprador.views import RegistroComprador


urlpatterns =  [

    url(r'^registrar$', RegistroComprador.as_view(), name='comprador_crear'),
]
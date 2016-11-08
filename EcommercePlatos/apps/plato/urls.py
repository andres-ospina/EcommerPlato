from django.conf.urls import url
from apps.plato.views import MostrarPlato,RegistrarPlato,plato_registrar,PlatoUpdate


urlpatterns =  [
    url(r'^listar$', MostrarPlato.as_view(), name='plato_listar'),
    url(r'^nuevo$',RegistrarPlato.as_view(), name='plato_crear'),
    url(r'^editar/(?P<pk>\d+)$', PlatoUpdate.as_view(), name='plato_editar'),
]
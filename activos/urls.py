from django.urls import path
from activos.views import tipo_activo, software, hardware, unido,TipoActivo

urlpatterns = [
    path('tipo_activo/', tipo_activo, name='tipo_activo'),
    path('software/', software, name='software'),
    path('hardware/', hardware, name='hardware'),
    path('unido/', unido, name='unido'),
    path('tipo/',TipoActivo, name= 'TipoActivo' )
]

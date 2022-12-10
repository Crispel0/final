from django.urls import path
from activos.views import tipo_activo, software, hardware

urlpatterns = [
    path('tipo_activo/', tipo_activo, name='tipo_activo'),
    path('software/', software, name='software'),
    path('hardware/', hardware, name='hardware'),
]

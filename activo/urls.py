from django.urls import path
from .views import registrar_activo

urlpatterns = [
    path('activo/', registrar_activo, name='activo'),
]

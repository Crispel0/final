from django.urls import path
from usuarios.views import usuarios, usuarios_crear,usuarios_editar,usuarios_eliminar 

urlpatterns = [
    path('usuarios/',usuarios,name="usuarios"),
    path('usuarios_crear/', usuarios_crear, name="usuarios_crear"),
    path('usuarios_editar/<int:pk>/', usuarios_editar, name="usuarios_editar"),
    path('usuarios_eliminar/<int:pk>/',usuarios_eliminar,name="usuarios_eliminar"),
    ]
   


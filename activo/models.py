from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class TipoActivo(models.Model):
    marca = models.CharField(max_length =50, null=False, blank=False, verbose_name= "marca")
    serie = models.CharField(max_length=30, null=False, blank=False, unique=True,verbose_name= "Nro de serie")
    class Activo(models.TextChoices):
        computador = '0', _('Computador')
        impresora = '1', _('Impresora')
    tipo_activo= models.CharField(max_length=1, choices=Activo.choices, verbose_name="Tipo de activo")
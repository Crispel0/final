from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class TipoActivo(models.Model):
    marca = models.CharField(max_length = 60, null=False, blank=False, verbose_name= "marca")
    serie = models.CharField(max_length=90, null=False, blank=False, unique=True,verbose_name= "Nro de serie")
    class Activo(models.TextChoices):
        computador = '0', _('Computador')
        impresora = '1', _('Impresora')
    tipo_activo= models.CharField(max_length=1, choices=Activo.choices, verbose_name="Tipo de activo")


class RegistroActivo(models.Model):
    fecha_creacion = models.DateField(auto_now_add = True)
    tipo_activo =models.ForeignKey(TipoActivo, on_delete=models.CASCADE)

class Tipo(models.Model):
    Hardware = '1'
    Software = '2'

    LEVEL_CHOICES = (
        (Hardware, 'Hardware'),
        (Software, 'Software'),
    )
    tipo = models.CharField(max_length=15, choices=LEVEL_CHOICES)

class Software(models.Model):     
    class SistemaOperativo(models.TextChoices):
        Windows = '0', _('Windows')
        linux = '1', _('Linux')
        Mac = '2', _('Mac')
    sistema_operativo= models.CharField(max_length=1, choices=SistemaOperativo.choices, verbose_name="Sistema operativo")

    class VersionSistemaOp(models.TextChoices):
        windows7 = '0', _('Windows 7')
        windows8 = '1', _('windows 8.1')
        windows10 = '2', _('windows 10')
        windows11 = '3', _('windows 11')
        debian = '4' , _('debian')
        ubuntu = '5' , _('ubuntu')
        mint = '6', _('mint')
        fedora = '7', _('fedora')
        manjaro = '8', _('manjaro')
        catalina = '9', _('catalina')
        sierra = '10', _('sierra')
        monterrey = '11', _('monterrey')
        bigsurf = '12', _('bigsufr')
    version_sistema_op= models.CharField(max_length=2, choices=VersionSistemaOp.choices, verbose_name="Versión sistema operativo")
    
    class Ofimatica(models.TextChoices):
         moffice= '0', _('Microsoft office') 
         loffice= '1', _('Libre office')
         ooffice= '2', _('Open office')
         ninguno = '3',_("No instalado")
    ofimatica= models.CharField(max_length=1, choices=Ofimatica.choices,  verbose_name="Ofimatica")

    class VersionOfimatica(models.TextChoices):
        v2007 ='0',_("2007")
        v2010 ='1',_("2010")
        v2013 ='2',_("2013")
        v2016 ='3',_("2016")
        v2019 ='4',_("2019")
        v365 ='5',_("365")
        v735 = '6',_("7.3.5")
        v734 = '7',_("7.3.4")
        v733 = '8',_("7.3.3")
        v732 = '9',_("7.3.2")
        v731 = '10',_("7.3.1")
        v413 = '11',_("4.1.3")
        v412 = '12',_("4.1.2")
        v411 = '13',_("4.1.1")
        v410 = '14',_("4.1.0")
        v400 = '15',_("4.0.0")
        ninguno = '16',_("No instalado")        
    version_ofimatica=models.CharField(max_length=3, choices=VersionOfimatica.choices, verbose_name="Versión ofimatica")

    class Antivirus(models.TextChoices):
        endpoint = '0', _('endpoint')
        avast = '1',_('avast')
        avg = '2',_('avg')
        kaspersky = '3' ,_('kaspersky')
        malwarebytes= '4',_('malwarebytes')
        bullguard= '5', _('bullguard')
        ninguno= '6', _("No instalado")
    antivirus=models.CharField(max_length=2, choices=Antivirus.choices, default=Antivirus.ninguno, verbose_name="Antivirus")

    class Navegador(models.TextChoices):
        edge= '0', _('microsoft edge')
        firefox= '1', _('mozilla firefox')
        crhome= '2', _('google chrome')
        opera= '3', _('opera')
        safari= '4', _('safari')
        ninguno= '5', _("No instalado")
    navegador= models.CharField(max_length=1, choices=Navegador.choices, default=Navegador.ninguno, verbose_name="Navegador web")

    class Navegador2(models.TextChoices):
        edge= '0', _('microsoft edge')
        firefox= '1', _('mozilla firefox')
        crhome= '2', _('google chrome')
        opera= '3', _('opera')
        safari= '4', _('safari')
        ninguno= '5', _("No instalado")
    navegador2= models.CharField(max_length=1, choices=Navegador2.choices, default=Navegador2.ninguno, verbose_name="Navegador web2")

    class HerramientaCloud(models.TextChoices):
        gdrive= '0', _('google drive')
        odrive= '1', _('one drive')
        dropbox= '2', _('dropbox')
        amazon= '3', _('amazon cloud')
        ninguno= '4', _('No instalado')
    herramienta_cloud= models.CharField(max_length=1, choices=HerramientaCloud.choices, verbose_name="Herramienta Cloud")
    
class Hardware(models.Model):

    modelo = models.CharField(max_length = 100, verbose_name= "modelo")
    capacidad = models.CharField(max_length = 100, verbose_name= "capacidad")
    no_aplica = models.CharField(max_length = 100, verbose_name= "no aplica")
    

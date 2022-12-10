from django.forms import ModelForm, widgets
from .models import Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model= Usuario
        exclude=['estado','user']
        widgets={
            'fecha_nacimiento': widgets.DateInput(attrs={'type':'date'})
        }


class UsuarioUpdateForm(ModelForm):
    class Meta:
        model= Usuario
        exclude=['estado','user']
        
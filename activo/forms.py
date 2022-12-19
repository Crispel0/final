from django import forms
from .models import TipoActivo


class TipoActivoForm(forms.ModelForm):
    class Meta:
        model = TipoActivo
        fields = '__all__'
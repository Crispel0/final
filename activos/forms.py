from django import forms
from .models import Tipo, Software, Hardware


class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = (
            'tipo',
        )

class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = '__all__'

class HardwareForm(forms.ModelForm):
    class Meta:
        model = Hardware
        fields = '__all__'
from django import forms
from .models import Tipo, Software, Hardware, TipoActivo


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
        exclude=['relacion']

class HardwareForm(forms.ModelForm):
    class Meta:
        model = Hardware
        fields = '__all__'
        exclude=['relacion']
        
class TipoActivoForm(forms.ModelForm):
    class Meta:
        model = TipoActivo
        fields = '__all__'
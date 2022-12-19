from django.shortcuts import redirect, render
from .forms import TipoActivoForm
from django.contrib.auth.decorators import login_required
from .models import TipoActivo
from django.contrib import messages
# Create your views here.

@login_required(login_url='inicio')
def registrar_activo(request):
    titulo="Registrar activo"
    form= TipoActivoForm()
    activos= TipoActivo.objects.all
    print (activos)
    context={
        'titulo':titulo,
        'form': form,
        'activos':activos,   
    }  
    if request.method == 'POST':  
        form = TipoActivoForm(request.POST)
        activo = form.save(commit=False)
        activo.save()
        return render(request, 'activo/activo.html',context)
    else:
        return render(request, 'activo/activo.html',context)
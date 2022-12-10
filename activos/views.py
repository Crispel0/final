from django.shortcuts import render, redirect
from .forms import TipoForm, SoftwareForm, HardwareForm
# Create your views here.

def tipo_activo(request):
    titulo="Tipo Activo"
    form= TipoForm()
    context={
        'titulo':titulo,
        'form': form    
    }  
    if request.method == 'GET':  
        return render(request, 'activos/tipo_activo.html',context)
    else:
        select=(request.POST['tipo'])
        if select == "Hardware":
            return redirect ('hardware')
        else:
            return redirect('software')
    
    
def software(request):
    titulo= "formulario Software"
    form= SoftwareForm()
    context={
        'titulo':titulo,
        'form': form
    }
    return render(request, 'activos/software.html', context)



def hardware(request):
    titulo= "formulario Hardware"
    form= HardwareForm()
    context={
        'titulo':titulo,
        'form': form
    }
    return render(request, 'activos/software.html', context)
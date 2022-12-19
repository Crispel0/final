from django.shortcuts import render, redirect
from .forms import TipoForm, SoftwareForm, HardwareForm,TipoActivoForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='inicio')
def tipo_activo(request):
    titulo="Tipo Activo"
    form= TipoForm()
    context={
        'titulo':titulo,
        'form': form    
    }  
    if request.method == 'GET':  
        return render(request, 'activos/unido.html',context)
    else:
        select=(request.POST['tipo'])
        if select == "1":
            return redirect ('hardware')
        else:
            return redirect('software')
    
@login_required(login_url='inicio')
def software(request):
    titulo= "formulario Software"
    form= SoftwareForm()
    context={
        'titulo':titulo,
        'form': form
    }
    return render(request, 'activos/software.html', context)


@login_required(login_url='inicio')
def hardware(request):
    titulo= "formulario Hardware"
    form= HardwareForm()
    context={
        'titulo':titulo,
        'form': form
    }
    return render(request, 'activos/hardware.html', context)

@login_required(login_url='inicio')
def unido(request):
    titulo="Tipo Activo"
    form= TipoForm()
    software= SoftwareForm()
    hardware= HardwareForm()
    form2=""
    context={
        'titulo':titulo,
        'form': form,    
        'software': software,
        'hardware': hardware,
        'form2': form2
    }
    if request.method == 'GET':  
        return render(request, 'activos/unido.html',context)
    else:
        select=(request.POST['tipo'])
        print(select)
        if select == "1":
            form= SoftwareForm()
            form2= hardware
            context={'titulo':titulo,
                     'form': form,  
                     'form2': form2
                    }
            return render (request, 'activos/info_activo.html', context)
        else:
            form2= software
            context={'titulo':titulo,
                     'form': form,  
                     'form2': form2
                    }
            return render (request, 'activos/unido.html', context)
        
      
        
@login_required(login_url='inicio')
def TipoActivo(request):
    form= TipoActivoForm()
    titulo="Modificado Tipo Activo"
    context={
        'form': form,
        'titulo':titulo,
    }
    if request.method == 'GET':
        return render (request, 'activos/tipo_Activo.html', context)
    else:
        select=(request.POST['tipo_activo'])
        print(select)
        form= HardwareForm()
        form2= SoftwareForm()
        context={'titulo':titulo,
                 'form': form,  
                 'form2': form2
                }
        return render (request,'activos/info_Activo.html', context)
        
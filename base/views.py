from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='inicio')
def index(request):
    titulo= 'Bienvenido'
    context={'titulo':titulo}
    return render(request, 'index.html', context)
    

def salir(request):
    logout(request)
    return redirect('inicio')

    
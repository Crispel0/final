from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout


def index(request):
    titulo= 'Bienvenido'
    context={'titulo':titulo}
    return render(request, 'index.html', context)
    

def salir(request):
    logout(request)
    return redirect('inicio')

    
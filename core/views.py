from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.
def home_visita(request):
    return render(request, 'home_visita.html')

def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                #registrar usuario
                user= User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('admin_usuarios')
            except IntegrityError:
                return render(request, 'registro.html',{
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                    })
        return render(request, 'registro.html',{
            'form': UserCreationForm,
            "error": 'Contraseñas no coinciden'
            })
    
def admin_usuarios(request):
    return render(request, 'admin_usuarios.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('home_visita')

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'iniciar_sesion.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, usuername=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iniciar_sesion.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecto'
                })
        else:
            login(request, user)
            return redirect('admin_usuarios')
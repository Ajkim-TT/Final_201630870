from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CrearUsuario
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def main_pag(request):
    return render(request,'principal.html')
def login_pag(request):
    if request.user.is_authenticated:
        return redirect('principal')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password) 
            if user is not None:
                login(request,user)
                return redirect('principal')
            else:
                messages.info(request,'USUARIO O CONTRASEÑA INCORRECTA')
    
        context = {}
        return render(request,"login.html",context)

def register_pag(request):
    if request.user.is_authenticated:
        return redirect('principal')
    else:
        formulario = CrearUsuario()
        if request.method == 'POST':
            formulario = CrearUsuario(request.POST)
            if formulario.is_valid():
                formulario.save()
                usuario = formulario.cleaned_data.get('username')
                messages.success(request, 'Cuenta creada para '+ usuario)
                return redirect('login')
        usuario = formulario.cleaned_data.get('username')
        messages.success(request, 'Error en los datos '+ usuario)
        context = {'form':formulario}
        return render(request,"register.html",context)

def logout_page(request):
    logout(request)
    return redirect('login')
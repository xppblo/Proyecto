from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth.models import User
from .services import crear_usuario
# Create your views here.

def index(request):
    inmuebles = Inmueble.objects.all()
    tipo_inmuebles = TipoInmueble.objects.all()
    context = {
        'inmuebles': inmuebles,
        'tipo_inmuebles': tipo_inmuebles
    }
    return render(request,'index.html', context)

def registro(request):
    
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        
        user = User.objects.create_user(username, email, password)
        
        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]
        user.save()
        
        rut = request.POST["rut"]
        telefono = request.POST["telefono"]
        tipo_usuario = TipoUsuario.objects.get(pk=2)
        
        usuario = Usuario(user=user, rut=rut, telefono=telefono, tipo_usuario=tipo_usuario)
        usuario.save()
        
        return redirect("/accounts/login")
    else:
        return render(request,"registro.html",{})
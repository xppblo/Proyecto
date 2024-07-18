from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from .forms import UsuarioForm
from .services import crear_usuario
# Create your views here.

def index(request):
    inmuebles = Inmueble.objects.all()
    tipo_inmuebles = TipoInmueble.objects.all()
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    context = {
        'inmuebles': inmuebles,
        'tipo_inmuebles': tipo_inmuebles,
        'lista_regiones': regiones,
        'lista_comunas': comunas
    }
    return render(request,'index.html', context)

@login_required
def bienvenido(request):
    inmuebles = Inmueble.objects.filter()
    tipo_inmuebles = TipoInmueble.objects.all()
    context = {
        'inmuebles': inmuebles,
        'tipo_inmuebles': tipo_inmuebles
    }
    return render(request,'bienvenido.html', context)

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

@login_required
def usuario_actualizar(request):
    if request.method == 'POST':
        u_form = UsuarioForm(request.POST,instance=request.user.usuario)
        if u_form.is_valid():
            u_form.save()
            return HttpResponseRedirect('/')
        
        
    else:
        u_form = UsuarioForm(instance=request.user.usuario)
        context={
            'u_form': u_form
        }
        return render(request,'usuario_actualizar.html', context)
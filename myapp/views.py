from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from .forms import UsuarioForm, InmuebleForm
from django.views import generic
# Create your views here.

def index(request):
    inmuebles = Inmueble.objects.filter(arrendado = False)
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
    inmuebles = Inmueble.objects.filter(usuarios= request.user.usuario.id)
    context = {
        'inmuebles': inmuebles,
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

#Crear Inmueble

@login_required
@login_required
def crear_inmueble(request):    
    if request.method == "POST":
        u_form = InmuebleForm(request.POST)
        if u_form.is_valid():
            inmueble = u_form.save(commit=False)  
            inmueble.save()
            inmueble.usuarios.add(request.user.id)
            return redirect('lista_inmueble')  # Redirigir a la lista de inmuebles
        else:
            # Imprimir los datos y errores del formulario en la consola para depuración
            print("Formulario no válido")
            print(u_form.errors)
            print(request.POST)
    else:
        u_form = InmuebleForm()  # Crear un formulario vacío

    context = {
        'form': u_form,
    }
    return render(request, "crear_inmueble.html", context)
    
"""
#Crear inmueble
@login_required
def crear_inmueble(request):    
    if request.method == "POST":
        u_form = InmuebleForm(request.POST)
        if u_form.is_valid():
            nombre = u_form.cleaned_data['nombre']
            direccion = u_form.cleaned_data['direccion']
            depto = u_form.cleaned_data['depto']
            m2_construidos = u_form.cleaned_data['m2_construidos']
            m2_totales = u_form.cleaned_data['m2_totales']
            estacionamientos = u_form.cleaned_data['estacionamientos']
            habitaciones = u_form.cleaned_data['habitaciones']
            banios = u_form.cleaned_data['banios']
            precio = u_form.cleaned_data['precio']
            tipo_inmueble = u_form.cleaned_data['tipo_inmueble']
            comuna = u_form.cleaned_data['comuna']
            region = u_form.cleaned_data['region']
            descripcion = u_form.cleaned_data['descripcion']
            
            inmu = Inmueble(nombre=nombre,
                            direccion=direccion,
                            depto=depto,
                            m2_construidos=m2_construidos,
                            m2_totales=m2_totales,
                            estacionamientos=estacionamientos,
                            habitaciones=habitaciones,
                            banios=banios,
                            precio=precio,
                            tipo_inmueble=tipo_inmueble,
                            comuna=comuna,
                            region=region,
                            descripcion=descripcion)
            inmu.save()
            
            inmu.usuarios.add(request.user.usuario.id)
            
            return HttpResponseRedirect('/lista_inmueble')
    else:
        context = {
            'form': InmuebleForm(),
        }
    return render(request, "crear_inmueble.html",context)

"""

#Editar inmueble
@login_required
def editar_inmueble(request, pk):
    inmueble = get_object_or_404(Inmueble, pk=pk, usuarios=request.user.usuario)
    if request.method == 'POST':
        form = InmuebleForm(request.POST, request.FILES, instance=inmueble)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/lista_inmueble')
    else:
        form = InmuebleForm(instance=inmueble)
        
        regiones = Region.objects.all()
        comunas = Comuna.objects.all()  # Filtrar comunas por la región del inmueble    
        return render(request, 'editar_inmueble.html', {'form': form, 'regiones': regiones, 'comunas': comunas})
    
#Borrar inmueble
@login_required
def borrar_inmueble(request, pk):
    inmueble = get_object_or_404(Inmueble, pk=pk, usuarios=request.user.usuario)
    if request.method == 'POST':
        inmueble.delete()
        messages.success(request, 'Inmueble borrado exitosamente')
        return redirect('lista_inmueble')
    
    return render(request, 'borrar_inmueble.html', {'inmueble': inmueble})

def ver_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, id=id)
    return render(request, 'ver_inmueble.html', {'inmueble': inmueble})
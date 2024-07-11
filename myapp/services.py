from django.contrib.auth.models import User
from myapp.models import Usuario, TipoUsuario, Region, Comuna, TipoInmueble, Inmueble

def crear_tipo_usuario(nombre):
    tipo_usuario = TipoUsuario(nombre=nombre)
    tipo_usuario.save()
    return tipo_usuario

def crear_usuario(nombre, apellido, tipo_usuario_id, telefono, rut):
    tipo_usuario = TipoUsuario.objects.get(id=tipo_usuario_id)
    usuario = Usuario(nombre=nombre, apellido=apellido, tipo_usuario=tipo_usuario, rut=rut, telefono=telefono)
    usuario.save()
    return usuario

def crear_region(nombre):
    region = Region(nombre=nombre)
    region.save()
    return region

def crear_comuna(nombre, region_id):
    region = Region.objects.get(id=region_id)
    comuna = Comuna(nombre=nombre, region=region)
    comuna.save()
    return comuna

def crear_tipo_inmueble(nombre):
    tipo_inmueble = TipoInmueble(nombre=nombre)
    tipo_inmueble.save()
    return tipo_inmueble

def crear_inmueble(nombre, descripcion, m2_construidos, m2_totales, cantidad_estacionamientos, cantidad_habitaciones, cantidad_banos, direccion, tipo_inmueble_id, precio_mensual, arrendador_id, region_id, comuna_id):
    tipo_inmueble = TipoInmueble.objects.get(id=tipo_inmueble_id)
    arrendador = Usuario.objects.get(id=arrendador_id)
    region = Region.objects.get(id=region_id)
    comuna = Comuna.objects.get(id=comuna_id)
    
    inmueble = Inmueble(
        nombre=nombre,
        descripcion=descripcion,
        m2_construidos=m2_construidos,
        m2_totales=m2_totales,
        cantidad_estacionamientos=cantidad_estacionamientos,
        cantidad_habitaciones=cantidad_habitaciones,
        cantidad_banos=cantidad_banos,
        direccion=direccion,
        tipo_inmueble=tipo_inmueble,
        precio_mensual=precio_mensual,
        arrendador=arrendador,
        region=region,
        comuna=comuna
    )
    inmueble.save()
    return inmueble

def listar_inmuebles():
    return Inmueble.objects.all()

def actualizar_inmueble(id, **kwargs):
    inmueble = Inmueble.objects.get(id=id)
    for key, value in kwargs.items():
        setattr(inmueble, key, value)
    inmueble.save()
    return inmueble

def eliminar_inmueble(id):
    inmueble = Inmueble.objects.get(id=id)
    inmueble.delete()
    return None
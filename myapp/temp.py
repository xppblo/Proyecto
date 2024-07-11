import os, django, time

os.environ.setdefault("DJANGO_SETTINGS_MODULE","arriendo.settings")
django.setup()

from myapp.models import Inmueble, Region, Comuna

#def obtener_inmuebles_comuna(comuna_id):
def obtener_inmuebles_comuna(comuna_nombre):
    select = '''
            select inmu.id, inmu.nombre,
            comuna.name as comuna, region.name as region
            from miapp_inmueble inmu
            inner join miapp_comuna comuna
            on inmu.comuna_id = comuna.id
            inner join miapp_region region
            on inmu.region_id = region.id
            where comuna.name LIKE '%'''+str(comuna_nombre)+'''%'
            '''
    data_inmuebles = Inmueble.objects.raw(select)

    archivo = open("inmueble_comuna.txt", "w")

    for inmu in data_inmuebles:
        archivo.write(inmu.id +'-' +inmu.nombre +'\n')

    archivo.close()


def obtener_inmueble(nombre, descripcion):
    lista_inmuebles = Inmueble.objects.filter(nombre__contains=nombre).filter(descripcion__contains=descripcion)

    archivo = open("inmueble_nombre_des.txt", "w")

    for inmu in lista_inmuebles:
        archivo.write(inmu +'\n')

    archivo.close()
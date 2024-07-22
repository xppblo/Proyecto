from django import forms
from .models import *
from django_select2 import forms as s2forms
'''
class InmuebleForm(forms.Form):
    comunas = [(x.id,x.name) for x in list(Comuna.objects.filter())]
    comuna = forms.ChoiceField(choices=comunas)
    regiones = [(x.id,x.name) for x in list(Region.objects.filter())]
    region = forms.ChoiceField(choices=regiones)
    nombre = forms.CharField(label='Nombre Inmueble', max_length=100)
    descripcion = forms.CharField(label='Descripción del Inmueble', max_length=100)
    direccion = forms.CharField(label='Dirección',max_length=100)
    depto = forms.CharField(label='Departamento',max_length=100)
    m2_construidos = forms.CharField(label='M2 construidos',max_length=100)
    m2_totales = forms.CharField(label='M2 totales',max_length=100)
    estacionamientos = forms.CharField(label='Numero de estacionamientos',max_length=100)
    habitaciones = forms.CharField(label='Numero de habitaciones',max_length=100)
    banios = forms.CharField(label='Numero de baños',max_length=100)
    precio = forms.CharField(label='Precio del Inmueble',max_length=100)
    tipos = TipoInmueble.objects.all().order_by('nombre').values_list('id','nombre')
    tipo_inmueble = forms.CharField(label='Tipo de Inmueble',required=True, widget=forms.Select(choices=tipos))
    
 '''

class UsuarioForm(forms.ModelForm):
    #rut = forms.CharField(label='Rut')
    telefono = forms.CharField(label='Teléfono')
    
    class Meta:
        model = Usuario
        fields = ['telefono']
        
class RegionWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        'name__icontains',
    ]
    
class ComunaWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        'nombre__icontains',
    ]

class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = [
            'nombre',
            'direccion',
            'depto',
            'm2_construidos',
            'm2_totales',
            'estacionamientos',
            'habitaciones',
            'banios',
            'precio',
            'tipo_inmueble',
            'region',
            'comuna',
            'descripcion'
            ]
        widgets = {
            'nombre':forms.TextInput(attrs={'class': 'form-control'}),
            'direccion':forms.TextInput(attrs={'class': 'form-control'}),
            'depto':forms.NumberInput(attrs={'class': 'form-control','min':'0','value':'0'}),
            'm2_construidos':forms.NumberInput(attrs={'class': 'form-control','min':'0','value':'0'}),
            'm2_totales':forms.NumberInput(attrs={'class': 'form-control','min':'0','value':'0'}),
            'estacionamientos':forms.NumberInput(attrs={'class': 'form-control','min':'0','max':'10','value':'0'}),
            'habitaciones':forms.NumberInput(attrs={'class': 'form-control','min':'0','max':'10','value':'0'}),
            'banios':forms.NumberInput(attrs={'class': 'form-control','min':'0','max':'10','value':'0'}),
            'precio':forms.NumberInput(attrs={'class': 'form-control','min':'0','value':'0'}),
            'tipo_inmueble':forms.Select(attrs={'class': 'form-control'}),
            'comuna': ComunaWidget(attrs={'class': 'form-control'}),
            'region': RegionWidget(attrs={'class': 'form-control'}),
            'descripcion':forms.Textarea(attrs={'class': 'form-control','rows':'2','cols':'10'})
        }

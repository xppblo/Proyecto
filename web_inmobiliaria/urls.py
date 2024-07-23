"""
URL configuration for web_inmobiliaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp.views import index, registro, bienvenido, usuario_actualizar, crear_inmueble,editar_inmueble, borrar_inmueble, ver_inmueble

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('registro/', registro, name='registro'),
    path('lista_inmueble', bienvenido, name='lista_inmueble'),
    path("usuario/actualizar", usuario_actualizar, name='usuario_actualizar'),
    #path("crear/inmueble",InmuebleCreateView.as_view(), name="crear-inmueble"),
    path("inmueble/crear", crear_inmueble, name='crear_inmueble'),
    path('inmueble/<int:pk>/editar/', editar_inmueble, name='editar_inmueble'),
    path('inmueble/<int:pk>/borrar/', borrar_inmueble, name='borrar_inmueble'),
    path('inmueble/<int:id>/ver/', ver_inmueble, name='ver_inmueble'),
    path("select2/", include("django_select2.urls")), 
    path('accounts/', include('django.contrib.auth.urls')),
]


"""weeza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path
import accs.views
import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.home, name='home'),
    path('aderir', accs.views.WorkerModelCreateView, name='aderir'),
    path('limpezadecasa', main.views.houseCleaning, name='limpezadecasa'),
    path('canalizacao', main.views.plumbing, name='canalizacao'),
    path('electricidade', main.views.electricity, name='electricidade'),
    path('frioeclimatizacao', main.views.cold_and_air_conditioning,
         name='frioeclimatizacao'),
    path('lavagemdecarro', main.views.car_washing,
         name='lavagemdecarro'),
    path('mecanica', main.views.mechanic,
         name='mecanica'),
    path('serralheiro', main.views.lock_smith,
         name='serralheiro'),
    path('reparodeelectronicos', main.views.electronic_device_repair,
         name='reparodeelectronicos'),



]

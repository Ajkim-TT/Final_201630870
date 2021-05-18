"""final_201630870 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from Login import views as vLog
from . import views as vFinal
from Aereolinea import views as vAereo

urlpatterns = [
    path('admin/',      admin.site.urls,    name = 'admin'),
    path('login/',      vLog.login_pag,     name = 'login'),
    path('logout/',     vLog.logout_page,   name = 'logout'),
    path('register/',   vLog.register_pag,  name = 'register'),
    path('principal/',  vLog.main_pag,    name = 'principal'),
    path('ordenar/',    vAereo.Ordenar,     name = 'ordenar'),
    path('factura/',    vAereo.Factura,     name = 'factura'),
    path('historial/',   vAereo.historial,   name = 'historial'),
]

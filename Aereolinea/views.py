from django.shortcuts import render
from Aereolinea.models import VueloFactura
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def Ordenar(request):
    return render(request,"pagina_orden.html")

@login_required(login_url='login')
def historial(request):
    inputsss = VueloFactura.objects.all()
    if request.method == 'POST':
        VueloFactura.objects.all().delete()
        inputsss = VueloFactura.objects.all()
        return render(request,"bitacora.html",{'entradas':inputsss})
    return render(request,"bitacora.html",{'entradas':inputsss})

@login_required(login_url='login')
def Factura(request):
    descuento = 0
    descuento = int(descuento)
    total_servicios_com = int(0)
    total_servicios_beb = int(0)
    total_servicios_pel = int(0)

    subtot_com = int(0)
    subtot_beb = int(0)
    subtot_pel = int(0)

    classe = request.GET["clase"]
    directorio = {'classe':classe}
    if request.GET.get("cant_com1",False):
        comida_clase1 = int(request.GET["cant_com1"])
        total_servicios_com = total_servicios_com + comida_clase1
        subtot_com = subtot_com + 50*comida_clase1
        directorio["NoCom1"]=comida_clase1
    if request.GET.get("cant_beb1",False):
        bebida_clase1 = int(request.GET["cant_beb1"])
        total_servicios_beb = total_servicios_beb + bebida_clase1
        subtot_beb = subtot_beb + 35*bebida_clase1
        directorio["NoBeb1"]=bebida_clase1
    if request.GET.get("cant_pel1",False):
        peli_clase1 = int(request.GET["cant_pel1"])
        total_servicios_pel = total_servicios_pel + peli_clase1
        subtot_pel = subtot_pel + 70*peli_clase1
        directorio["NoPel1"]=peli_clase1
    if request.GET.get("cant_com2",False):
        comida_clase2 = int(request.GET["cant_com2"])
        total_servicios_com = total_servicios_com + comida_clase2
        subtot_com = subtot_com + 40*comida_clase2
        directorio["NoCom2"]=comida_clase2
    if request.GET.get("cant_beb2",False):
        bebida_clase2 = int(request.GET["cant_beb2"])
        total_servicios_beb = total_servicios_beb + bebida_clase2
        subtot_beb = subtot_beb + 25*bebida_clase2
        directorio["NoBeb2"]=bebida_clase2
    if request.GET.get("cant_pel2",False):
        peli_clase2 = int(request.GET["cant_pel2"])
        total_servicios_pel = total_servicios_pel + peli_clase2
        subtot_pel = subtot_pel + 55*peli_clase2
        directorio["NoPel2"]=peli_clase2
    if request.GET.get("cant_com3",False):
        comida_clase3 = int(request.GET["cant_com3"])
        total_servicios_com = total_servicios_com + comida_clase3
        subtot_com = subtot_com + 25*comida_clase3
        directorio["NoCom3"]=comida_clase3
    if request.GET.get("cant_beb3",False):
        bebida_clase3 = int(request.GET["cant_beb3"])
        total_servicios_beb = total_servicios_beb + bebida_clase3
        subtot_beb = subtot_beb + 10*bebida_clase3
        directorio["NoBeb3"]=bebida_clase3
    if request.GET.get("cant_pel3",False):
        peli_clase3 = int(request.GET["cant_pel3"])
        total_servicios_pel = total_servicios_pel + peli_clase3
        subtot_pel = subtot_pel + 25*peli_clase3
        directorio["NoPel3"]=peli_clase3
    
    total_servicios = total_servicios_beb + total_servicios_com + total_servicios_pel
    subtotal_t = subtot_com + subtot_beb + subtot_pel
    if classe == "primera":
        if (int(subtot_com)>0) and (int(subtot_beb)>0) and (int(subtot_pel)>0):
            descuento = descuento + subtotal_t*0.05
        else:
            descuento = descuento
    else:
        descuento = descuento

    if int(total_servicios)>10:
        descuento = descuento + subtotal_t*0.10
    else: 
        descuento = descuento
    Total = float(subtotal_t) - float(descuento)
    Total = float(Total)
    
    directorio['Subtot']=subtotal_t
    directorio['Desc']=descuento
    directorio['Total']=Total

    newdata = VueloFactura(
        cajero = request.GET.get('user'),
        clase= classe,
        comida = int(total_servicios_com),
        bebida = int(total_servicios_beb),
        pelicula = int(total_servicios_pel),
        servicios = int(total_servicios ),
        subtotal = subtotal_t,
        descuentoM = descuento,
        total = Total,
    )
    newdata.save()

    return render(request,"pagina_factura.html",directorio)
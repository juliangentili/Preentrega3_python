from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from appcoder.models import *
from .forms import *





def inicio(req):
    return render(req , "index.html")


def neumaticos(req):
    return render(req,"neumaticos.html")


def tuercas(req):
    return render(req , "tuercas.html")


def usuarios(req):
    return render(req,"usuarios.html")


def formulario_rueda(req):
   print("method" , req.method)
   print("POST" , req.POST)

   if req.method == "POST":
      miformulario = neumaticoFormulario(req.POST)
      if miformulario.is_valid():
         
         data = miformulario.cleaned_data

         neumatico = Neumatico(marca=data["marca"],rodado=data["rodado"])
         neumatico.save()
         return render (req , "index.html")
   else:
       miformulario= neumaticoFormulario
       return render(req , "formulario_rueda.html" , {"miformulario": miformulario})
       
def tuercas_formulario(req):
   print("method" , req.method)
   print("POST" , req.POST)

   if req.method == "POST":
      form_ruedas = Antirrobo(req.POST)
      if form_ruedas.is_valid():
         data = form_ruedas.cleaned_data
         tuerca = Antirrobo(marca=data["marca"],precio=data["precio"])
         tuerca.save()
         return render (req , "index.html")
   else:
       form_ruedas= Antirrobo()

   return render (req, "formulario_tuercas.html", {"form_ruedas": form_ruedas})           
   

def busquedaNeumatico(req):

    return render(req , "busquedaNeumatico.html")

  
def buscar(req):
    marca = req.GET.get("marca", "")

    if marca:
        neumaticos = Neumatico.objects.filter(marca__icontains=marca)
        return render(req, "resultado.html", {"marca": marca, "neumaticos": neumaticos})
    else:
        return HttpResponse("Debe ingresar la marca del neumático.")

    return HttpResponse(f"Buscando el neumático con marca: {marca}")



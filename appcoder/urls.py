from django.urls import path
from appcoder.views import *


urlpatterns = [
    path('neumaticos/', neumaticos , name="neumaticos"),
    path('tuercas/', tuercas , name="tuercas"),
    path('usuario/', usuarios , name="usuarios"),
    path('', inicio , name="inicio"),
    path('agregar_rueda/<marca>/<ancho>/<relacion>/<rodado>/<valor>/', neumaticos),
    path('formulario_rueda/', formulario_rueda , name="formulario_rueda"),
    path('tuercas_formulario/', tuercas_formulario , name="tuercas_formulario"),
    path('busqueda_neumatico/',busquedaNeumatico , name="busquedaNeumatico"),
    path('buscar/',buscar , name="buscar"),
]
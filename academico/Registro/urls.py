from django.urls import path, include
from . import views
from django.contrib.auth.views import login_required

urlpatterns = [
    
    # listar las carreras de la bd
    # localhost:8000/listarCarreras 
    path('listarCarreras', views.listar_carreras, name="listar_carreras"),

    # agregar una carrera
    # localhost:8000/agregar_carrera
    path('agregar_carrera', views.agregar_carrera, name="agregar_carrera"),    
    
    # borrar una carrera
    # localhost:8000/borrar_carrera/NUM
    path('borrar_carrera/<int:carrera_id>', views.borrar_carrera, name="borrar_carrera"),

    # editar una carrera
    # localhost:8000/editar_carrera/NUM
    path('editar_carrera/<int:carrera_id>', views.editar_carrera ,name="editar_carrera"),

    # OTROS LLAMADOS CON GENERICS
    # localhost:8000/add_carrera
    path('add_carrera', views.CarreraCreate.as_view(), name="add_carrera"),

    path('list_carreras', views.CarreraList.as_view(), name="list_carreras"),

    # Crear la ruta para eliminar y modificar por GENERICS    
    path('del_carrera/<pk>', views.CarreraDelete.as_view(), name="del_carrera"),
    
    path('update_carrera/<pk>', views.CarreraUpdate.as_view(), name="update_carrera"),
    
    
]
from django.shortcuts import render, redirect
from .models import Carrera
from .forms import CarreraForm

# las clases genericas
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# esta libreria nos permitira redireccionamiento
from django.urls import reverse_lazy



def listar_carreras(request):
    # esto es un SELECT * FROM CARRERA
    carreras = Carrera.objects.all()
    # AHORA ESTAMOS LLEVANDO el listado de carreras
    # para desplegar en el template
    return render(request, "Registro/listar_carreras.html", 
                  {'carreras': carreras})
    
def agregar_carrera(request):
    if request.method == "POST":
        form = CarreraForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/agregar_carrera")
    else:
        form = CarreraForm()
        return render(request, "Registro/agregar_carrera.html", {'form': form})
 
def borrar_carrera(request, carrera_id):
    # Recuperamos la instancia de la carrera y la borramos
    instancia = Carrera.objects.get(id=carrera_id)
    instancia.delete()
 
    # Después redireccionamos de nuevo a la lista
    return redirect('listar_carreras')
 
def editar_carrera(request, carrera_id):
    # Recuperamos la instancia de la carrera
    instancia = Carrera.objects.get(id=carrera_id)
 
    # Creamos el formulario con los datos de la instancia
    form = CarreraForm(instance=instancia)
 
    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = CarreraForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manipular antes de grabar
            instancia = form.save(commit=False)
            # Podemos guardar cuando queramos
            instancia.save()
 
    # Si llegamos al final renderizamos el formulario
    return render(request, "Registro/editar_carrera.html", {'form': form})



#------------CLASES GENERICS-----------------------------------------------
# --Otra forma usando clases Generics -------
class CarreraCreate(CreateView):
    model = Carrera
    form_class = CarreraForm
    template_name = 'Registro/carrera_form.html'
    success_url = reverse_lazy("add_carrera")

class CarreraList(ListView):
    model = Carrera
    template_name = 'Registro/list_carreras.html'
    # paginate_by = 4

class CarreraUpdate(UpdateView):
    model = Carrera
    form_class = CarreraForm
    template_name = 'Registro/carrera_form.html'
    success_url = reverse_lazy('list_carreras')

        

class CarreraDelete(DeleteView):
    model = Carrera
    template_name = 'Registro/carrera_delete.html'
    success_url = reverse_lazy('list_carreras')
 


 

    
    
from re import A
from django.contrib import admin
from .models import Carrera, Alumno

# Register your models here.
admin.site.register(Carrera)
admin.site.register(Alumno)

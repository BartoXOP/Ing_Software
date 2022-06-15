from django.urls import path, include
from . import views
from .views import RegistroUsuario, UserList
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    
    # localhost:8000/usuario/registrar
    path('registrar', RegistroUsuario.as_view(), name="registrar"),
    path('listar', UserList.as_view(), name="list_user"),

    path('login/', auth_views.LoginView.as_view(template_name='Usuario/login.html'), name='login'),

    # Login and Logout
    path('login/', LoginView.as_view(redirect_authenticated_user=True,template_name='Usuario/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='Usuario/logout.html'), name='logout'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('donacion/', TemplateView.as_view(template_name='Usuario/donacion.html'), name='donacion'),

]

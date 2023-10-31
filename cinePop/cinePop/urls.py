from django.contrib import admin
from django.urls import path
from app_inicial_e_cadastro import views

urlpatterns = [
    # rota, view responsável, nome de referência
    # páginal inicial cine
    path('',views.home,name='home'),
    path('cadastro',views.cadastro,name='cadastro'),
    path('login', views.login, name='login'),
    path('usuarios', views.usuarios, name='listagem_usuarios'),
    path('admin/', admin.site.urls),
]

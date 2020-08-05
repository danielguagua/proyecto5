from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path
from core import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('quienes_somos/', views.quienes_somos, name="quienes_somos"),
    path('servicios/', views.servicios, name="servicios"),
    path('login/', views.login, name="login"),
    path('inventario/', views.inventario, name="inventario"),
    path('usuarios/', views.usuarios, name="usuarios"),
    path('admin/', admin.site.urls),
]

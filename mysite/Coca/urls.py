from django.urls import path
from . import views

urlpatterns = [
    path('', views.coca_index, name='Coca_list'),

    path('perfil', views.coca_perfil, name='coca_perfil'),
    path('inicio', views.coca_inicio, name='inicio'),
    path('sesion', views.sesion, name='sesion'),
    path('crear_prueba', views.crear_prueba, name='crear_prueba'),
    path('crear_reporte', views.crear_reporte, name='crear_reporte'),
    path('ver_pruebas', views.ver_pruebas, name='ver_pruebas'),
    path('ver_reportes', views.ver_reportes, name='ver_reportes'),
    path('trabajadores', views.trabajadores, name='trabajadores'),
    path('404', views.error, name='error'),
]
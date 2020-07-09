from django.shortcuts import render

# Create your views here.
def coca_index(request):
    return render(request, 'index.html', {})

def sesion(request):
    return render(request, 'login.html', {})

def coca_inicio(request):
    return render(request, 'index.html', {})

def coca_perfil(request):
    return render(request, 'perfil.html', {})

def crear_prueba(request):
    return render(request, 'crear_prueba.html', {})

def crear_reporte(request):
    return render(request, 'crear_reporte.html', {})

def ver_reportes(request):
    return render(request, 'ver_reportes.html', {})

def ver_pruebas(request):
    return render(request, 'ver_pruebas.html', {})

def trabajadores(request):
    return render(request, 'trabajadores.html', {})

def error(request):
    return render(request, '404.html', {})


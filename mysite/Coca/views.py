from django.shortcuts import render

# Create your views here.
def coca_index(request):
    return render(request, 'Coca/templates/index.html', {})

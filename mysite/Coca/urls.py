from django.urls import path
from . import views

urlpatterns = [
    path('', views.coca_index, name='Coca_list'),
]
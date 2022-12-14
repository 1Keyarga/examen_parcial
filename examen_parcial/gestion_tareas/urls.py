from . import views
from django.urls import path

app_name = 'gestion_tareas'

urlpatterns = [
        
    path('', views.ingreso, name='ingreso'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('eliminar/<int:idTarea>', views.eliminaRegistro, name='eliminaRegistro'),
    path('ver/<int:idTarea>', views.verTarea, name='verTarea')
]
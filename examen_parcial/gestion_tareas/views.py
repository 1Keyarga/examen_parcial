from django.shortcuts import render,redirect
from .models import usuario
from .models import tarea
# Create your views here.


def ingreso(request):
    #usuarios ordenados
    usuariosRegistrados = usuario.objects.all().order_by('id')
    valor = 0
    if 'Loguearse' in request.POST:
        #capturo codigo y contraseña de los usuarios
        codigo = request.POST.get('Usuario')  
        contraseña = request.POST.get('Contrasenha')  
        #para todos los usuarios registrados
        
        for usuariosBase in usuariosRegistrados:
            if usuariosBase.codigo == codigo and usuariosBase.contraseña == contraseña:
                 valor = 1
        
        if valor == 1:
            return redirect('gestion_tareas:dashboard')
        elif valor == 0:
            return redirect('gestion_tareas:ingreso')
    
    return render(request,'gestion_tareas/vistaIngreso.html')


def dashboard(request):
    
    tareasUsuario = tarea.objects.all().order_by('id')
    
    if 'Salida' in request.POST:
        
        return redirect('gestion_tareas:ingreso')
    
    
    
    
    return   render(request,'gestion_tareas/dashboard.html',{
        'tareasUsuario':tareasUsuario
    })
    

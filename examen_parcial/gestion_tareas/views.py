from django.shortcuts import render,redirect
from .models import usuario
from .models import tarea
from datetime import date
from datetime import datetime
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
    
   # elif  'Eliminar' in request.POST:
        
         #idElimina = request.POST.get('valor') 
        # print(idElimina)
        # eliminarID = tarea.objects.get(id=idElimina)
         #eliminarID.delete()
     
    elif 'Crear' in request.POST:
        #agarramos el dia de hoy
        fechaCreacionPrima = datetime.now()
        #actualizamos el dia de hoy como dias/mes/año
        fechaCreacionPrima.strftime("%d/%m/%Y")
        
             

    return  render(request,'gestion_tareas/dashboard.html',{
        'tareasUsuario':tareasUsuario
    })
    
    

def eliminaRegistro(request, idTarea):
    #obtiene el registro igual al id
    tareas = tarea.objects.get(id = idTarea)
    #elimina el registro con el id igual
    tareas.delete()
    #redirecciona a la pagina padre acabando la funcion
    return redirect('gestion_tareas:dashboard')


def verTarea(request, idTarea):
    #obtiene el registro igual al id
    tareaVisualizar = tarea.objects.get(id = idTarea)      
    #retorn el registro con el id igual
    return  render(request,'gestion_tareas/detalleTarea.html',{
        "tareaVisualizar": tareaVisualizar
    })


 
     

    
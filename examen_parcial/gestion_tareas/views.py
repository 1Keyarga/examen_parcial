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
    usuariosRegistrados = usuario.objects.all().order_by('id')
    #creamos una lista vacia que mandara los usuarios designados
   
   
    if 'Salida' in request.POST:
        
        return redirect('gestion_tareas:ingreso')
     
    elif 'Crear' in request.POST:
        #agarramos el dia de hoy
        fechaCreacionPrima = datetime.now()
    
        #obtenemos las variables pasadas
        tituloP = request.POST.get('tituloU')
        descripcionP = request.POST.get('descripcionU')
        fechaEntregaP = request.POST.get('fechaEntregaU')  
        usuarioDesignadoP = request.POST.get('usuarioDesignadoU')  
        tarea(titulo = str(tituloP), descripcion = str(descripcionP), fechaEntrega = str(fechaEntregaP),usuarioDesignado=str(usuarioDesignadoP),
              fechaCreacion = str(fechaCreacionPrima.strftime("%d/%m/%Y"))).save()
        tareasUsuario = tarea.objects.all().order_by('id')    
        
    elif 'Filtrar' in request.POST:
       
         filtrado = request.POST.get('filtradoDesignado')    
         tareasUsuario = tarea.objects.filter(usuarioDesignado=filtrado)  
         
    #ponemos al final el obtener lista designados para garantizar que despues de cualquier
    #request lo actualice  
    listaDesignados = []
    for  userDesign in tareasUsuario:
         #si el usuario no se encuentra en la lista entonces lo añade
         if userDesign.usuarioDesignado not in listaDesignados:
            listaDesignados.append(str(userDesign.usuarioDesignado))
    #llenamos todos los usarios existentes para poder elegir al usuario al que se le va a registrar 
    #o asignar dicha tarea        
    listaUsuarios = []
    
    for  user in usuariosRegistrados:
         #si el usuario no se encuentra en la lista entonces lo añade
         if user.codigo not in listaUsuarios:
            listaUsuarios.append(str(user.codigo))
            
    return  render(request,'gestion_tareas/dashboard.html',{'tareasUsuario':tareasUsuario, 'listaDesignados':listaDesignados, 'listaUsuarios':listaUsuarios})
    
    

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


 
     

    
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Alumno, Grado, Encargado,Encargados_alumnos,Pago,Examene,Papeleria,Actividade,Permiso,Asignacion_Permiso,Asignacion_Materia,Asignacion_Grado,Personal,Asignacion_Acividade,Asignacion_Punteo
from .forms import AlumnoForm,agregar_papeleriaForm,Asignacion_PunteoForm,Asignacion_PermisoForm
from .forms import EncargadoForm,agregar_examenesForm,Asignacion_AcividadeForm,horasForm,PersonalForm
from .forms import MyForm,asignacion_encargadoForm, nueva_asignacion_encargadoForm,asignacion_alumnoForm,asignacion_pagosForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext, Template
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.apps import apps
import datetime

unidad= None
@login_required
def dashboard(request):
    today = datetime.datetime.now() 
    query_set = Group.objects.filter(user = request.user)
    actual=[]
    a = False;
    for g in query_set:
        if g.name=="Administracion":
            alumnos=Alumno.objects.filter(Estado__iexact="PendienteExamen")
            return render(request, 'administracion/dashboard_Administracion.html',{'alumnos': alumnos})
        if g.name=="Secretaria":
            alumnos=Alumno.objects.all()
            return render(request, 'administracion/dashboard_Secretaria.html',{'alumnos': alumnos})
        if g.name=="Alumno":
            return render(request, 'administracion/dashboard_Alumno.html')
        if g.name=="Maestro":
            mes = today.month
            actividades=Actividade.objects.filter(Grupo__iexact='Todos')
            for act in actividades:
                acti = {}
                if(int(act.Fecha_Inicio[5:7])==int(mes)):
                    acti['Titulo']=act.Titulo
                    acti['Fecha_Inicio']=act.Fecha_Inicio
                    actual.append(acti)
            encargado=Asignacion_Grado.objects.filter(Personal=Personal.objects.get(Usuario=request.user))
            materias=Asignacion_Materia.objects.filter(Personal=Personal.objects.get(Usuario=request.user))
            cursos = materias.count()
            return render(request, 'administracion/dashboard_Maestro.html', {'mes': mes,'cursos': cursos,'actual': actual,'materias': materias,'encargado': encargado})
    return render(request, 'administracion/dashboard_Secretaria.html')
@login_required
def actividades_cursos(request):
    try:
        cursos = Asignacion_Materia.objects.filter(Personal=Personal.objects.get(Usuario=request.user))
        Datos = []
        asignacion = []
        for curso in cursos:
            alumno   = Alumno.objects.filter(Grado=curso.Grado)
            asi = Asignacion_Acividade.objects.filter(Asignacion_Materia=curso)
            asignacion.append(asi.count())
            Datos.append(alumno.count())     
    except Asignacion_Materia.DoesNotExist:
        cursos=None
    request.session['informacion']= None
    request.session['errores']= None
    return render(request, 'administracion/actividades_maestros.html',{'cursos': cursos,'asignacion': asignacion,'Datos': Datos})

@login_required
def asignacion_actividades(request, pk):
    try:
        if request.method == "POST":
            a = request.POST['unidad']
        else:
            a= request.session['unidad']
        if a=="uni1":
            unidad="PRIMERA UNIDAD"
        if a=="uni2":
            unidad="SEGUNDA UNIDAD"
        if a=="uni3":
            unidad="TERCERA UNIDAD"
        if a=="uni4":
            unidad="CUARTA UNIDAD"
        request.session['unidad'] = a
        curso=Asignacion_Materia.objects.get(Grado=Grado.objects.get(pk=pk), Personal=Personal.objects.get(Usuario=request.user))
        actividades= Asignacion_Acividade.objects.filter(Asignacion_Materia=curso,Unidad=a)
        request.session['grado']=pk
        if request.session['informacion']:
            info= request.session['informacion']
        else:
            info = None
        if request.session['errores']:
            errores= request.session['errores']
        else:
            errores = None
    except Asignacion_Acividade.DoesNotExist:
            actividades=None
    return render(request, 'administracion/actividades_cursos.html',{'curso': curso, 'actividades': actividades,'unidad' : unidad,'info' : info,'errores' : errores})

@login_required
def nueva_actividad(request, pk):
    request.session['informacion']= None
    curso = Asignacion_Materia.objects.get(Grado=Grado.objects.get(pk=pk), Personal=Personal.objects.get(Usuario=request.user))
    asignaciones = Asignacion_Acividade.objects.filter(Asignacion_Materia = curso)
    errores = None
    informacion= None
    info= None
    total= int(0)
    unidad = request.session['unidad']
    actividades=Asignacion_Acividade.objects.filter(Asignacion_Materia = curso,Unidad=unidad)
    if request.method == "POST":
        form = Asignacion_AcividadeForm(request.POST)
        if curso :
            paso = True;
            if form.is_valid():
                post = form.save(commit=False)
                post.Asignacion_Materia= curso
                post.Unidad=unidad
                for asi in asignaciones:
                    if post.Unidad == asi.Unidad:
                        total=int(total)+int(asi.Ponderacion)
                    if post.Unidad == asi.Unidad and post.Nombre_Actividad == asi.Nombre_Actividad:  
                        paso= False;
                        errores="Ya Tienes Creado Esta Actividad Si Deseas Editarla Regresa Al Listado De Actividades"      
                if paso:
                    total=int(total)+int(post.Ponderacion)
                    if total>100:
                        total=int(total)-100-int(post.Ponderacion)
                        if total < 0: 
                            total = int(total)*-1
                        errores="La Ponderacion De Todas Las Actividades Suma Mas De 100 Puntos Te Restan " + str(total) + " Puntos Para Asignar Esta Unidad."      
                    else:
                        post.save()
                        total = 100-int(total)
                        if total == 0:
                            info="Esa Unidad Ya Esta Asignada Completamente"
                        else:
                            info="Te Quedan " + str(total) + " Puntos Para Asignar Esta Unidad"
                        informacion="Se Ha Guardado Con Exito Esta Actividad"   
    else:
        form = Asignacion_AcividadeForm()
    return render(request, 'administracion/nueva_actividad.html',{'form':form, 'curso': curso, 'errores': errores, 'informacion': informacion, 'info':info, 'unidad':unidad, 'actividades':actividades})

@login_required
def eliminar_actividad(request,pk):
    punteos = Asignacion_Punteo.objects.filter(Asignacion_Acividades=Asignacion_Acividade.objects.get(pk=pk))
    if punteos:
        request.session['errores']= "No se puede eliminar esta actividad actualmente esta asignada a un alumno con una nota, asigne 0 a la actividad en notas para poder continuar..."
        request.session['informacion']=None
    else:
        request.session['errores']=None
        Asignacion_Acividade.objects.get(pk=pk).delete()
        request.session['informacion']= "Se Ha Eliminado Con Exito La Actividad" 
    return redirect('asignacion_actividades',pk=request.session['grado'])


@login_required
def notas(request):
    query_set = Group.objects.filter(user = request.user)
    a = "NO"
    for g in query_set:
        if g.name=="Alumno":
            a="Alumno"
        if g.name=="Maestro":
            a="Maestro"
    if a=="Maestro":
        try:
            cursos = Asignacion_Materia.objects.filter(Personal=Personal.objects.get(Usuario=request.user))
            Datos = []
            asignacion = []
            for curso in cursos:
                alumno   = Alumno.objects.filter(Grado=curso.Grado)
                try:
                    asi = Asignacion_Grado.objects.get(Grado=curso.Grado).Personal
                except Exception as e:
                    asi = "No Asignado"
                asignacion.append(asi)
                Datos.append(alumno.count())
               
        except Asignacion_Materia.DoesNotExist:
            cursos=None
    else:
        cursos=None
    return render(request, 'administracion/Notas_Maestros.html', {'cursos': cursos,'asignacion': asignacion,'Datos': Datos})

@login_required
def asignacion_notas(request, pk):
    try:
        request.session['informacion']= None
        request.session['errores']= None
        if request.method == "POST":
            a = request.POST['unidad']
        else:
            a= request.session['unidad']
        if a=="uni1":
            unidad="PRIMERA UNIDAD"
        if a=="uni2":
            unidad="SEGUNDA UNIDAD"
        if a=="uni3":
            unidad="TERCERA UNIDAD"
        if a=="uni4":
            unidad="CUARTA UNIDAD"
        request.session['unidad'] = a
        curso=Asignacion_Materia.objects.get(Grado=Grado.objects.get(pk=pk), Personal=Personal.objects.get(Usuario=request.user))
        actividades= Asignacion_Acividade.objects.filter(Asignacion_Materia=curso,Unidad=a)
        alumnos=Alumno.objects.filter(Grado=Grado.objects.get(pk=pk))
        Notas = []
        total=[]
        tot=int(0)
        estado="No Aprobado"
        for alumno in alumnos:
            for actividad in actividades:
                nota = {}
                nota['Alumno'] = alumno.pk
                nota['Actividad'] = actividad.pk
                nota['act'] = actividad.Nombre_Actividad
                try:
                    nota['pk'] = Asignacion_Punteo.objects.get(Asignacion_Acividades=actividad, Alumno=alumno).pk
                    nota['Punteo'] = Asignacion_Punteo.objects.get(Asignacion_Acividades=actividad, Alumno=alumno).Nota
                    estado = Asignacion_Punteo.objects.get(Asignacion_Acividades=actividad, Alumno=alumno).Estado
                except Asignacion_Punteo.DoesNotExist:
                    nota['pk']="0"
                    nota['Punteo'] ="0"
                    estado="No Aprobado"
                tot=int(tot)+int(nota['Punteo'])
                Notas.append(nota)
            total.append(tot)
            tot=0
    except Asignacion_Acividade.DoesNotExist:
            actividades=None
    return render(request, 'administracion/asignacion_notas.html', {'curso': curso, 'actividades': actividades, 'alumnos': alumnos,'Notas' : Notas,'total' : total,'unidad' : unidad,'Estado' : estado})

@login_required
def estado_nota(request,pk):
    a = request.session['unidad']
    curso=Asignacion_Materia.objects.get(Grado=Grado.objects.get(pk=pk), Personal=Personal.objects.get(Usuario=request.user))
    actividades= Asignacion_Acividade.objects.filter(Asignacion_Materia=curso,Unidad=a)
    alumnos=Alumno.objects.filter(Grado=Grado.objects.get(pk=pk))
    try:
        for x in alumnos:
            l = Asignacion_Punteo.objects.get(pk=request.POST['pk'])
            modificar= Asignacion_PunteoForm(instance=l)
            al = modificar.save(commit=False)
            al.Nota=int(request.POST['value'])
            al.save()
    except Exception as e:
        a=None
    return render(request, 'administracion/nueva_nota.html', {'notas': notas})

def ponderar(request):
    try:
        int(request.POST['value'])
    except ValueError:
        _data = {'success': False, 'error_msg': 'Error, Solo debe ingresar numeros en esta actividad '}
        return JsonResponse(_data)
    if request.POST['value']=="0":
        Asignacion_Punteo.objects.get(pk=request.POST['pk']).delete()
        _data = {'success': True}
        return JsonResponse(_data)
    ponderacion=Asignacion_Acividade.objects.get(pk=request.POST['Actividad']).Ponderacion
    if int(request.POST['value'])>int(ponderacion):
        _data = {'success': False, 'error_msg': 'Error, La Nota es mas alta de lo que permite la actividad, nota maxima permitida: ' + ponderacion}
        return JsonResponse(_data)
    try:
        if request.POST['pk'] == "0":
            actividad=Asignacion_Acividade.objects.get(pk=request.POST['Actividad'])
            alumno=Alumno.objects.get(pk=request.POST['alumno'])
            Asignacion_Punteo.objects.create(Asignacion_Acividades=actividad, Alumno=alumno,Nota=request.POST['value'])
            _data = {'success': True}
            return JsonResponse(_data)
        if not 'name' in request.POST or not 'pk' in request.POST or not 'value' in request.POST:
            _data = {'success': False, 'error_msg': 'Error, Falta De Parametros '}
            return JsonResponse(_data)
        l = Asignacion_Punteo.objects.get(pk=request.POST['pk'])
        modificar= Asignacion_PunteoForm(instance=l)
        al = modificar.save(commit=False)
        al.Nota=int(request.POST['value'])
        al.save()
        _data = {'success': True}
        return JsonResponse(_data)
    except Exception as e:
        _data = {'success': False,
                'error_msg': f'Error Al Ingresar datos: {e}'}
        return JsonResponse(_data)

@login_required
def calendario(request):
    query_set = Group.objects.filter(user = request.user)
    a = False;
    actividad = Actividade.objects.all()
    for g in query_set:
        if g.name=="Administracion":
            actividad = Actividade.objects.all()
        if g.name=="Secretaria":
            actividad = Actividade.objects.all()
        if g.name=="Alumno":
            try:
                perfil = Alumno.objects.get(Usuario=request.user)
                grado=str(perfil.Grado)
                if "Diversificado" in grado:
                    actividad = Actividade.objects.filter(Grupo__iexact="estu-bach") | Actividade.objects.filter(Grupo__iexact='Todos')
                if "Basico" in grado:
                    actividad = Actividade.objects.filter(Grupo__iexact="estu-basico") | Actividade.objects.filter(Grupo__iexact='Todos')
                if "Primaria" in grado:
                    actividad = Actividade.objects.filter(Grupo__iexact="estu-primaria") | Actividade.objects.filter(Grupo__iexact='Todos')
                if "Pre-Primaria" in grado:
                    actividad = Actividade.objects.filter(Grupo__iexact="estu-preprimaria") | Actividade.objects.filter(Grupo__iexact='Todos')
            except Alumno.DoesNotExist:
                perfil=None
    return render(request, 'administracion/actividades.html', {'actividad': actividad})
@login_required
def calendario_info(request,pk):
    actividad = Actividade.objects.get(pk=pk)
    return render(request, 'administracion/calendario_info.html',{'actividad': actividad})

@login_required
def horario(request):
    return render(request, 'administracion/horario.html')
@login_required
def horas(request):
    if request.method == "POST":
        form = horasForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = horasForm()
    return render(request, 'administracion/horas.html',{'form': form})
@login_required
def horarios(request):
    return render(request, 'administracion/horarios.html')
@login_required
def horarios_grado(request):
    return render(request, 'administracion/horario_grado.html')

@login_required
def perfil(request):
    query_set = Group.objects.filter(user = request.user)
    a = "NO"
    for g in query_set:
        if g.name=="Alumno":
            a="Alumno"
    if a=="Alumno":
        try:
            perfil = Alumno.objects.get(Usuario=request.user)
        except Alumno.DoesNotExist:
            perfil=None
    else:
        perfil=None
    return render(request, 'administracion/perfil.html', {'perfil': perfil})


@login_required
def listado_permisos(request,pk):
    usuario=Personal.objects.get(pk=pk)
    if request.method == "POST":
        l = Asignacion_Permiso.objects.filter(Usuario=usuario.Usuario)
        todos=Permiso.objects.all()
        for x in todos:
            actividades=request.POST.get(x.Nombre, False)
            try:
                asign=Asignacion_Permiso.objects.get(Permiso=x, Usuario=usuario.Usuario)
            except Asignacion_Permiso.DoesNotExist:
                asign=None
            if asign in l:
                modificar= Asignacion_PermisoForm(instance=asign)
                al = modificar.save(commit=False)
                if(actividades=="on"):
                    al.Estado="Activo"
                else:
                    al.Estado="Inactivo"
                al.save()
            else:
                modificar= Asignacion_PermisoForm()
                al = modificar.save(commit=False)
                al.Permiso=x
                al.Usuario=usuario.Usuario
                if(actividades=="on"):
                    al.Estado="Activo"
                else:
                    al.Estado="Inactivo"
                al.save()     

    asignado = []
    usua=Asignacion_Permiso.objects.filter(Usuario=usuario.Usuario)
    for perm in usua:
        if(perm.Estado == "Activo"):
            asignado.append(perm.Permiso)
    return render(request, 'administracion/lista_permisos.html', {'asignado': asignado,'usuario': usuario,'usua': usua})
@login_required
def asignar_permisos(request):
    if request.method == "POST":
        usu=request.POST['usuario']
        if usu:
            return redirect('listado_permisos', pk=usu)
    Usuarios=Personal.objects.exclude(Usuario__isnull=True)
    return render(request, 'administracion/asignar_permisos.html', {'Usuarios': Usuarios})



@login_required
def ver_encargados(request):
    Encargados = Encargado.objects.filter(estado__iexact='Activo')
    return render(request, 'administracion/ver_encargados.html', {'Encargados': Encargados})

@login_required
def no_pago(request):
    return render(request, 'administracion/no_pago.html')

@login_required
def ver_pagos(request):
    pagos = Pago.objects.all()
    return render(request, 'administracion/ver_pagos.html', {'pagos': pagos})

@login_required
def asignacion_pagos(request):
    if request.method == "POST":
        form = asignacion_pagosForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if post.Tipo_Pago == "Inscripcion":
                modificar= AlumnoForm(instance=post.Alumno)
                al = modificar.save(commit=False)
                al.estado="Activo"
                al.save()
            post.save()
            return redirect('ver_pagos')
    else:
        form = asignacion_pagosForm()
    return render(request, 'administracion/asignacion_pago.html', {'form': form})

@login_required
def agregar_examenes(request):
    a=False
    if request.method == "POST":
        form = agregar_examenesForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            try:
                pago= Pago.objects.filter(Alumno=post.Alumno)
                for p in pago:
                    if p.Tipo_Pago == "Examen":
                        a=True
            except Pago.DoesNotExist:
                return redirect('no_pago')
            if a == True:
                if post.Estado_Examen == "Aprobado":
                    modificar= AlumnoForm(instance=post.Alumno)
                    al = modificar.save(commit=False)
                    al.estado="PendienteInscripcion"
                    al.save()
                if post.Estado_Examen == "Reprobado":
                    modificar= AlumnoForm(instance=post.Alumno)
                    al = modificar.save(commit=False)
                    al.estado="Inactivo"
                    al.save()
                post.fechaingreso = timezone.now()
                post.save()
                return redirect('ver_examenes')
            else:
                return redirect('no_pago')
    else:
        form = agregar_examenesForm()
    return render(request, 'administracion/agregar_examenes.html', {'form': form})

def error(request):
    form = MyForm()
    if request.method=='POST':
        form = MyForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            alumno = cd.get('codigo')
            try:
                alumnos = Alumno.objects.get(Codigo=alumno)
            except Alumno.DoesNotExist:
                return redirect('error')
            return redirect('papeleria', pk=alumnos.pk)
    else:
        form = MyForm()
    return render(request, 'administracion/error_404.html', {'form': form})

def buscar_papeleria(request):
    form = MyForm()
    if request.method=='POST':
        form = MyForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            alumno = cd.get('codigo')
            try:
                alumnos = Alumno.objects.get(Codigo=alumno)
            except Alumno.DoesNotExist:
                return redirect('error')
            return redirect('papeleria', pk=alumnos.pk)
    else:
        form = MyForm()
    return render(request, 'administracion/buscar_alumno.html', {'form': form})

def papelerias(request, pk):
    alumno = Alumno.objects.get(pk=pk)
    try:
        papeleria= Papeleria.objects.get(Alumno=alumno)
    except Papeleria.DoesNotExist:
        papeleria=None
    if request.method == "POST":
        form = agregar_papeleriaForm(request.POST, instance=papeleria)
        if form.is_valid():
            post = form.save(commit=False)
            post.alumno = Alumno.objects.get(pk=pk)
            post.save()
            return redirect('dashboard')
    else:
        form= agregar_papeleriaForm(instance=papeleria)
    return render(request, 'administracion/papeleria.html', {'form': form,'alumno':alumno})

@login_required
def ver_examenes(request):
    examenes = Examene.objects.all()
    return render(request, 'administracion/ver_examenes.html', {'examenes': examenes})

@login_required
def pago(request, pk):
    pago = get_object_or_404(Pago, pk=pk)
    return render(request, 'administracion/pagos.html', {'pago': pago})

@login_required
def estudiante(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    return render(request, 'administracion/estudiante.html', {'alumno': alumno})

@login_required
def nuevo_alumno(request):
    grados = Grado.objects.all()
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('../../alumno/nuevo/')

    else:
        form = AlumnoForm()
    return render(request, 'administracion/nuevo_alumno.html', {'form': form, 'grados': grados})

@login_required
def nuevo_encargado(request):
    if request.method == "POST":
        form = EncargadoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('encargado', pk=post.pk)
    else:
        form = EncargadoForm()
    return render(request, 'administracion/nuevo_encargado.html', {'form': form})

@login_required
def encargado(request, pk):
    encargado = Encargado.objects.get(pk=pk)
    encargados=Encargados_alumnos.objects.filter(encargado=encargado).distinct()
    if request.method == "POST":
        form = EncargadoForm(request.POST, instance=encargado)
        encargado = form.save(commit=False)
        encargado.save()
        return redirect('ver_encargados')
    else:
        form = EncargadoForm(instance=encargado)
        form1 = asignacion_alumnoForm(instance=encargado)
    return render(request, 'administracion/encargado.html', {'form': form,'form1': form1, 'encargado': encargado, 'encargados': encargados})

def agregar_papeleria(request, pk):
    alumnos = get_object_or_404(Alumno, pk=pk)
    try:
        papeleria= Papeleria.objects.get(Alumno=alumnos)
    except Papeleria.DoesNotExist:
        papeleria=None
    if request.method == "POST":
        form = agregar_papeleriaForm(request.POST, instance=papeleria)
        if form.is_valid():
            post = form.save(commit=False)
            post.Alumno = Alumno.objects.get(pk=pk)
            post.save()
            user = request.user
            if user.is_authenticated:
                return redirect('dashboard')
            else:
                return redirect('buscar_papeleria')
               
    else:
        form = agregar_papeleriaForm(instance=papeleria)
    return render(request, 'administracion/estudiante.html', {'form': form})

@login_required  
def alumno_editar(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    encargados=Encargados_alumnos.objects.filter(alumno=alumno).distinct()
    try:
        papeleria= Papeleria.objects.get(Alumno=alumno)
    except Papeleria.DoesNotExist:
        papeleria=None

    if request.method == "POST":
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.author = request.user
            alumno.published_date = timezone.now()
            alumno.save()
            return redirect('dashboard')
    else:
        form = AlumnoForm(instance=alumno)
        form1 = asignacion_encargadoForm(instance=alumno)
        form2= agregar_papeleriaForm(instance=papeleria)
    return render(request, 'administracion/estudiante.html', {'form': form,'form1': form1,'form2': form2,'alumno': alumno,'encargados': encargados})

@login_required
def nueva_asignacion_encargado(request):
    if request.method == "POST":
        form = nueva_asignacion_encargadoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('encargado', pk=post.pk)
    else:
        form = nueva_asignacion_encargadoForm()
    return render(request, 'administracion/asignacion_encargado.html', {'form': form})

@login_required
def asignacion_encargado(request, pk):
    if request.method == "POST":
        form = asignacion_encargadoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.alumno = Alumno.objects.get(pk=pk)
            post.save()
            return redirect('dashboard')
    else:
        form = asignacion_encargadoForm()
    return render(request, 'administracion/asignacion_encargado.html', {'form': form})

@login_required
def asignacion_alumno(request, pk):
    if request.method == "POST":
        form = asignacion_alumnoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.encargado = Encargado.objects.get(pk=pk)
            post.save()
            return redirect('encargado', pk=pk)
    else:
        form = nueva_asignacion_encargadoForm()
    return render(request, 'administracion/asignacion_encargado.html', {'form': form})

@login_required
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def asignar_usuariosAlumnos(request):
    alumnos = Alumno.objects.all()
    for alumno in alumnos:
        if(alumno.Codigo):
            if(alumno.Usuario):
                print("hola")
            else:
                try:
                    if(User.objects.get(username=alumno.Codigo)):
                        modificar = AlumnoForm(instance=alumno)
                        al = modificar.save(commit=False)
                        al.estado = "Registro"
                        al.Usuario=User.objects.get(username=alumno.Codigo)
                        al.save()
                except User.DoesNotExist:
                    usuario = User.objects.create_user(username=alumno.Codigo,password="Colegio123")
                    modificar = AlumnoForm(instance=alumno)
                    al = modificar.save(commit=False)
                    al.estado = "Registro"
                    al.Usuario=User.objects.get(username=alumno.Codigo)
                    al.save()
        else:
            print("No se puede")
               
    return render(request, 'administracion/usuarioasignado.html')

@login_required
def nuevopersonal(request):
    if request.method == "POST":
        form = PersonalForm(request.POST)
        if form.is_valid():
            usuario = User.objects.create_user(username=request.POST['Usuario'],password="Colegio123")
            post = form.save(commit=False)
            post.Usuario=User.objects.get(username=request.POST['Usuario'])
            post.save()
            return redirect('dashboard')
    else:
        form = PersonalForm()
    return render(request, 'administracion/nuevopersonal.html', {'form': form})
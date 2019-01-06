from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Alumno, Grado, Encargado,Encargados_alumnos,Pago,Examene,Papeleria,Actividade 
from .forms import AlumnoForm,agregar_papeleriaForm
from .forms import EncargadoForm,agregar_examenesForm
from .forms import MyForm,asignacion_encargadoForm, nueva_asignacion_encargadoForm,asignacion_alumnoForm,asignacion_pagosForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext, Template
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

@login_required
def dashboard(request):
    query_set = Group.objects.filter(user = request.user)
    a = False;
    for g in query_set:
        if g.name=="Administracion":
           return render(request, 'administracion/dashboard_Administracion.html')
        if g.name=="Secretaria":
           return render(request, 'administracion/dashboard_Secretaria.html')
        if g.name=="Alumno":
           return render(request, 'administracion/dashboard_Alumno.html')
    return render(request, 'administracion/dashboard.html')

@login_required
def calendario(request):
    actividad = Actividade.objects.all()
    return render(request, 'administracion/actividades.html', {'actividad': actividad})

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
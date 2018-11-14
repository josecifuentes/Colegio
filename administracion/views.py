from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Alumno, Grado, Encargado,Encargados_alumnos,Pago,Examene,Papeleria 
from .forms import AlumnoForm,agregar_papeleriaForm
from .forms import EncargadoForm,agregar_examenesForm
from .forms import asignacion_encargadoForm, nueva_asignacion_encargadoForm,asignacion_alumnoForm,asignacion_pagosForm
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
            a=True
    if a:
        alumnos = Alumno.objects.filter(estado__iexact='PendienteExamen')
    else:
        alumnos = Alumno.objects.all()
    return render(request, 'administracion/dashboard.html', {'alumnos': alumnos})

@login_required
def ver_encargados(request):
    Encargados = Encargado.objects.filter(estado__iexact='Activo')
    return render(request, 'administracion/ver_encargados.html', {'Encargados': Encargados})

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
            post.save()
            return redirect('ver_pagos')
    else:
        form = asignacion_pagosForm()
    return render(request, 'administracion/asignacion_pago.html', {'form': form})

@login_required
def agregar_examenes(request):
    if request.method == "POST":
        form = agregar_examenesForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.fechaingreso = timezone.now()
            post.save()
            return redirect('ver_examenes')
    else:
        form = agregar_examenesForm()
    return render(request, 'administracion/agregar_examenes.html', {'form': form})

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
            return redirect('estudiante', pk=post.pk)
    else:
           form = AlumnoForm()
    return render(request, 'administracion/nuevo_alumno.html', {'form': form, 'grados': grados})

@login_required
def agergar_papeleria(request, pk):
    if request.method == "POST":
        form = agregar_papeleriaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.alumno = Alumno.objects.get(pk=pk)
            post.save()
            return redirect('encargado', pk=pk)
    else:
        form = nueva_asignacion_encargadoForm()
    return render(request, 'administracion/asignacion_encargado.html', {'form': form})


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
    encargado = get_object_or_404(Encargado, pk=pk)
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

@login_required  
def alumno_editar(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    encargados=Encargados_alumnos.objects.filter(alumno=alumno).distinct()
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
    return render(request, 'administracion/estudiante.html', {'form': form,'form1': form1,'alumno': alumno,'encargados': encargados})

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
            return redirect('encargado', pk=post.pk)
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
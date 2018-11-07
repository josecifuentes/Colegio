from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Alumno
from .forms import AlumnoForm
from .forms import EncargadoForm
from .forms import asignacion_encargadoForm
from django.contrib.auth.decorators import login_required

def dashboard(request):
    alumnos = Alumno.objects.filter(estado__iexact='PendienteExamen')
    return render(request, 'administracion/dashboard.html', {'alumnos': alumnos})

def estudiante(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    return render(request, 'administracion/estudiante.html', {'alumno': alumno})

@login_required
def nuevo_alumno(request):
    form = AlumnoForm()
    return render(request, 'administracion/nuevo_alumno.html', {'form': form})
@login_required
def nuevo_encargado(request):
    form = EncargadoForm()
    return render(request, 'administracion/nuevo_encargado.html', {'form': form})
    
@login_required
def asignacion_encargado(request):
    form = asignacion_encargadoForm()
    return render(request, 'administracion/asignacion_encargado.html', {'form': form})


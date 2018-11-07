from django import forms
from .models import Alumno
from .models import Encargado
from .models import Ecargados_alumnos

class AlumnoForm(forms.ModelForm):

    class Meta:
        model = Alumno
        fields = ('Codigo', 'Primer_Nombre', 'Segundo_Nombre', 'Tercer_Nombre', 'Primer_Apellido', 'Segundo_Apellido', 'Grado', 'Genero', 'nacimiento', 'direccion', 'telefono', 'estado')

class EncargadoForm(forms.ModelForm):

    class Meta:
        model = Encargado
        fields = ('Nombres', 'Apellidos', 'telefono_celular', 'direccion', 'telefono_casa', 'Trabajo', 'telefono_trabajo', 'Dpi', 'estado')

class asignacion_encargadoForm(forms.ModelForm):

    class Meta:
        model = Ecargados_alumnos
        fields = ('alumno', 'encargado')
from django import forms
from .models import Alumno, Grado, Pago, Papeleria,Asignacion_Acividade,Asignacion_Punteo,Asignacion_Permiso,horas,Permiso,Asignacion_Materia
from .models import Encargado, Examene,Actividade
from .models import Encargados_alumnos,Personal,ContenidoExamen
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.admin import widgets
import datetime


class AlumnoForm(forms.ModelForm):

    class Meta:
        model = Alumno
        fields = ('Codigo', 'Primer_Nombre', 'Segundo_Nombre', 'Tercer_Nombre', 'Primer_Apellido', 'Segundo_Apellido', 'Grado','Seccion', 'Genero', 'nacimiento', 'direccion', 'telefono','telefono2')
        widgets = {
        	'Codigo': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese Un Codigo Valido Ej.2019-000...'}),
  			'Primer_Nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba El Primer Nombre Del Alumno'}),
 			'Segundo_Nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba El Segundo Nombre Del Alumno'}),
 			'Tercer_Nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba El Tercer Nombre Del Alumno'}),
 			'Primer_Apellido': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba El Primer Apellido Del Alumno'}),
 			'Segundo_Apellido': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba El Segundo Apellido Del Alumno'}),
 			'Grado': forms.Select(attrs={'class': 'chosen-select','data-placeholder': 'Seleccione Un Grado...'}),
 			'Seccion': forms.Select(attrs={'class': 'form-control custom-select-value'}),
 			'Genero': forms.Select(attrs={'class': 'form-control custom-select-value'}),
 			'nacimiento': forms.TextInput(attrs={'class': 'form-control','value': '2000-01-01'}),
			'direccion': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba La Direccion Del Alumno'}),
 			'telefono': forms.TextInput(attrs={'class': 'form-control','data-mask': '9999-9999','placeholder': 'Máximo 8 dígitos...'}),
            'telefono2': forms.TextInput(attrs={'class': 'form-control','data-mask': '9999-9999','placeholder': 'Máximo 8 dígitos...'}),
  			
        }

class EncargadoForm(forms.ModelForm):

    class Meta:
        model = Encargado
        fields = ('Nombres', 'Apellidos', 'telefono_celular', 'direccion', 'telefono_casa', 'Trabajo', 'telefono_trabajo', 'Dpi', 'estado')
        widgets = {
            'Nombres': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba Los Nombres Del Encargado'}),
            'Apellidos': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba Los Apellidos Del Encargado'}),
            'telefono_celular': forms.TextInput(attrs={'class': 'form-control','data-mask': '9999-9999','placeholder': 'Máximo 8 dígitos...'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba La Direccion Del Encargado'}),
            'telefono_casa': forms.TextInput(attrs={'class': 'form-control','data-mask': '9999-9999','placeholder': 'Máximo 8 dígitos...'}),
            'Trabajo': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba El Lugar De Trabajo Del Encargado'}),
            'telefono_trabajo': forms.TextInput(attrs={'class': 'form-control','data-mask': '9999-9999','placeholder': 'Máximo 8 dígitos...'}),
            'Dpi': forms.TextInput(attrs={'class': 'form-control','data-mask': '9999-99999-9999','placeholder': 'Máximo 13 dígitos...'}),
            'estado': forms.Select(attrs={'class': 'form-control custom-select-value'}),
        }    
class asignacion_encargadoForm(forms.ModelForm):

    class Meta:
        model = Encargados_alumnos
        fields = ('encargado','parentesco')
        widgets = {
            'encargado': forms.Select(attrs={'class': 'chosen-select','data-placeholder': 'Seleccione Un Encargado...'}),
            'parentesco': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba El Parentesco Del Alumno Con El Encargado'}),
        }    
class nueva_asignacion_encargadoForm(forms.ModelForm):

    class Meta:
        model = Encargados_alumnos
        fields = ('alumno','encargado','parentesco')
        widgets = {
            'alumno': forms.Select(attrs={'class': 'chosen-select','data-placeholder': 'Seleccione Un Alumno...'}),
            'encargado': forms.Select(attrs={'class': 'chosen-select','data-placeholder': 'Seleccione Un Encargado...'}),
            'parentesco': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba El Parentesco Del Alumno Con El Encargado'}),
        }
class asignacion_alumnoForm(forms.ModelForm):

    class Meta:
        model = Encargados_alumnos
        fields = ('alumno','parentesco')
        widgets = {
            'alumno': forms.Select(attrs={'class': 'chosen-select','data-placeholder': 'Seleccione Un Encargado...'}),
            'parentesco': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba El Parentesco Del Alumno Con El Encargado'}),
        }   
class asignacion_alumnoForm(forms.ModelForm):

    class Meta:
        model = Encargados_alumnos
        fields = ('alumno','parentesco')
        widgets = {
            'alumno': forms.Select(attrs={'class': 'chosen-select','data-placeholder': 'Seleccione Un Encargado...'}),
            'parentesco': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba El Parentesco Del Alumno Con El Encargado'}),
        }  
class asignacion_pagosForm(forms.ModelForm):

    class Meta:
        model = Pago
        fields = ('Boleta','Alumno','Cantidad','Comentario','Tipo_Pago')
        widgets = {
            'Boleta': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba La Boleta De Pago Del Alumno'}),
            'Alumno': forms.Select(attrs={'class': 'chosen-select','data-placeholder': 'Seleccione Un Alumno...'}),
            'Cantidad': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba La Cantidad Total Del Pago'}),
            'Comentario': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Comentario Al Pago Del Alumno'}),
            'Tipo_Pago': forms.Select(attrs={'class': 'chosen-select','data-placeholder': 'Seleccione El Pago...'}),
        }  

class agregar_papeleriaForm(forms.ModelForm):

    class Meta:
        model = Papeleria
        fields = ('Padre','Madre','Alergias','Enfermedades','Nombre_Doctor','Telefono_Doctor', 'Cui','Partida_Nacimiento','Certificado_Pre_Primaria','Certificado_Primaria','Certificado_Basico','Certificado_Bachillerato','Tipo_Sangre','Comentarios')
        widgets = {
            'Padre': forms.Select(attrs={'class': 'chosen-select','data-placeholder': 'Seleccione El Padre Del Alumno...'}),
            'Madre': forms.Select(attrs={'class': 'chosen-select','data-placeholder': 'Seleccione La Madre Del Alumno...'}),
            'Alergias': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Liste Las Alergias Del Alumno, Separe Por ,'}),
            'Enfermedades': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Comentario Al Pago Del Alumno'}),
            'Nombre_Doctor': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Comentario Al Pago Del Alumno'}),
            'Telefono_Doctor': forms.TextInput(attrs={'class': 'form-control','data-mask': '9999-9999','placeholder': 'Máximo 8 dígitos...'}),
            'Cui': forms.TextInput(attrs={'class': 'form-control','data-mask': '9999-99999-9999','placeholder': 'Máximo 13 dígitos...'}),
            'Partida_Nacimiento': forms.Select(attrs={'class': 'form-control custom-select-value'}),
            'Certificado_Pre_Primaria': forms.Select(attrs={'class': 'form-control custom-select-value'}),
            'Certificado_Primaria': forms.Select(attrs={'class': 'form-control custom-select-value'}),
            'Certificado_Basico': forms.Select(attrs={'class': 'form-control custom-select-value'}),
            'Certificado_Bachillerato': forms.Select(attrs={'class': 'form-control custom-select-value'}),
            'Tipo_Sangre': forms.Select(attrs={'class': 'form-control custom-select-value'}),
            'Partida_Nacimiento': forms.Select(attrs={'class': 'form-control custom-select-value'}),
            'Comentarios': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba Alguna Anotacion'}),
          }  
          
class agregar_examenesForm(forms.ModelForm):

    class Meta:
        model = Examene
        fields = ('Boleta','Nota_Idioma','Comentario_Idioma','Estado_Idioma','Nota_Matematicas','Comentario_Matematicas','Estado_Matematicas','Nota_Ingles','Comentario_Ingles','Estado_Ingles')
        widgets = {
            'Boleta': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba La Boleta De Pago Del Alumno'}),
            'Nota_Idioma': forms.TextInput(attrs={'class': 'form-control','data-mask': '999','placeholder': 'Máximo 3 dígitos...'}),
            'Comentario_Idioma': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Agrege un Comentario a la nota del examen'}),
            'Estado_Idioma': forms.Select(attrs={'class': 'chosen-select','data-placeholder': 'Seleccione el estado de la nota...'}),
            'Nota_Matematicas': forms.TextInput(attrs={'class': 'form-control','data-mask': '999','placeholder': 'Máximo 3 dígitos...'}),
            'Comentario_Matematicas': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Agrege un Comentario a la nota del examen'}),
            'Estado_Matematicas': forms.Select(attrs={'class': 'chosen-select','data-placeholder': 'Seleccione el estado de la nota...'}),
            'Nota_Ingles': forms.TextInput(attrs={'class': 'form-control','data-mask': '999','placeholder': 'Máximo 3 dígitos...'}),
            'Comentario_Ingles': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Agrege un Comentario a la nota del examen'}),
            'Estado_Ingles': forms.Select(attrs={'class': 'chosen-select','data-placeholder': 'Seleccione el estado de la nota...'}),
        }  

class MyForm(forms.Form): #Notar que no hereda de forms.ModelForm
    
    codigo = forms.CharField()

class Asignacion_AcividadeForm(forms.ModelForm):

    class Meta:
        model = Asignacion_Acividade
        fields = ('Nombre_Actividad','Descripcion_Actividad','Ponderacion')
        widgets = {
            'Nombre_Actividad': forms.Select(attrs={'class': 'chosen-select','data-placeholder': 'Seleccione Una Actividad...'}),
            'Descripcion_Actividad': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Describa a Continuacion Como Se Calificara La Actividad'}),
            'Ponderacion': forms.TextInput(attrs={'class': 'touchspin1'}),
        }  

class Asignacion_PunteoForm(forms.ModelForm):

    class Meta:
        model = Asignacion_Punteo
        fields = ('Alumno','Nota')
        widgets = {
            'Alumno': forms.Select(attrs={'class': 'chosen-select','data-placeholder': 'Seleccione Un Alumno...'}),
            'Nota': forms.TextInput(attrs={'class': 'touchspin1'}),
        } 

class Asignacion_notasForm(forms.ModelForm):

    class Meta:
        model = Asignacion_Punteo
        fields = ('Alumno','Nota')
        widgets = {
            'Alumno': forms.Select(attrs={'class': 'chosen-select','data-placeholder': 'Seleccione Un Alumno...'}),
            'Nota': forms.TextInput(attrs={'class': 'touchspin1'}),
        }  

class Asignacion_PermisoForm(forms.ModelForm):

    class Meta:
        model = Asignacion_Permiso
        fields = ('Permiso','Usuario','Estado')
        widgets = {
            'Permiso': forms.Select(attrs={'class': 'chosen-select','data-placeholder': 'Seleccione Un Permiso...'}),
            'Usuario': forms.Select(attrs={'class': 'chosen-select','data-placeholder': 'Seleccione Un Usuario...'}),
            'Estado': forms.Select(attrs={'class': 'chosen-select','data-placeholder': 'Seleccione Un estado...'}),
        }  

class horasForm(forms.ModelForm):

    class Meta:
        model = horas
        fields = ('Nivel','hora_inicio','hora_fin')
        widgets = {
            'Nivel': forms.Select(attrs={'class': 'chosen-select','data-placeholder': 'Seleccione Un Nivel...'}),
            'hora_inicio': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Seleccione Hora de inicio'}),
            'hora_fin': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Seleccione Hora de Fin'}),
              }  

class PersonalForm(forms.ModelForm):

    class Meta:
        model = Personal
        fields = ('Primer_Nombre', 'Segundo_Nombre', 'Primer_Apellido', 'Segundo_Apellido',
         'Telefono_Casa', 'Telefono_Celular', 'Direccion','Dpi', 'Estado_Civil', 
         'Fecha_Nacimiento', 'Lugar_Nacimiento', 'No_Hijos','Nit',
          'Fecha_Inicio_Labores','Nivel_Academico', 'Titulo', 'Cedula_Docente',
          'Registro_Escalafonario', 'Salario','Hora_Entrada', 'Hora_Salida','email')
        widgets = {
            'Primer_Nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba El Primer Nombre Del Alumno'}),
            'Segundo_Nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba El Segundo Nombre Del Alumno'}),
            'Primer_Apellido': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba El Primer Apellido Del Alumno'}),
            'Segundo_Apellido': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba El Segundo Apellido Del Alumno'}),
            'Telefono_Casa': forms.TextInput(attrs={'class': 'form-control','data-mask': '9999-9999','placeholder': 'Máximo 8 dígitos...'}),
            'Telefono_Celular': forms.TextInput(attrs={'class': 'form-control','data-mask': '9999-9999','placeholder': 'Máximo 8 dígitos...'}),
            'Direccion': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese la direccion'}),
            'Dpi': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese el Dpi'}),
            'Estado_Civil': forms.Select(attrs={'class': 'form-control custom-select-value'}),
            'Fecha_Nacimiento': forms.TextInput(attrs={'class': 'form-control','value': '01/01/2000'}),
            'Lugar_Nacimiento': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese lugar de nacimiento'}),
            'No_Hijos': forms.Select(attrs={'class': 'form-control custom-select-value'}),
            'Nit': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese el nit'}),
            'Fecha_Inicio_Labores': forms.TextInput(attrs={'class': 'form-control','value': '01/01/2000'}),
            'Nivel_Academico': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese el nivel academico'}),
            'Titulo':  forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese el titulo que tiene'}),
            'Cedula_Docente': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese la cedula de docente'}),
            'Registro_Escalafonario':  forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese el registro escalafonario'}),
            'Salario':  forms.TextInput(attrs={'class': 'form-control','data-mask': '9999','placeholder': 'Máximo 4 dígitos...'}),
            'Hora_Entrada': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Seleccione Hora de entrada'}),
            'Hora_Salida':forms.TextInput(attrs={'class': 'form-control','placeholder': 'Seleccione Hora de salida'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba el email'}),
            
        }
class calendarioForm(forms.ModelForm):

    class Meta:
        model = Actividade
        fields = ('Titulo','Descripcion','Especifico','Lugar','Fecha_Inicio','Fecha_Fin','Grupo')
        widgets = {
            'Grupo': forms.Select(attrs={'class': 'chosen-select','data-placeholder': 'Seleccione Un Grupo...'}),
            'Titulo': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba el titulo que le dara a la actividad','autocomplete':'off'}),
            'Descripcion': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Describa brevemente la actividad','autocomplete':'off'}),
            'Especifico': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Describa con detalles la actividad','autocomplete':'off'}),
            'Lugar': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba el lugar de la actividad','autocomplete':'off'}),
            'Fecha_Inicio': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Seleccione la fecha de Inicio',}),
            'Fecha_Fin': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Seleccione la fecha de finalizacion',}),
              } 

class InicioForm(forms.ModelForm):

    class Meta:
        model = Alumno
        fields = ('Primer_Nombre', 'Segundo_Nombre', 'Tercer_Nombre', 'Primer_Apellido', 'Segundo_Apellido', 'Genero', 'nacimiento', 'direccion', 'telefono','telefono2')
        widgets = {
            'Primer_Nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba El Primer Nombre Del Alumno','readonly':'true'}),
            'Segundo_Nombre': forms.TextInput(attrs={'class': 'form-control','readonly':'true'}),
            'Tercer_Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Primer_Apellido': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba El Primer Apellido Del Alumno','readonly':'true'}),
            'Segundo_Apellido': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba El Segundo Apellido Del Alumno','readonly':'true'}),
            'Genero': forms.Select(attrs={'class': 'form-control custom-select-value'}),
            'nacimiento': forms.TextInput(attrs={'class': 'form-control','readonly':'true'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control','data-mask': '9999-9999'}),
            'telefono2': forms.TextInput(attrs={'class': 'form-control','data-mask': '9999-9999'}),
            
        }

class permisoForm(forms.ModelForm):

    class Meta:
        model = Permiso
        fields = ('Nombre','Descripcion')
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Seleccione Hora de inicio'}),
            'Descripcion': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Seleccione Hora de inicio'}),
              }  

class GradonivelForm(forms.Form):
    grado = forms.ModelChoiceField(
        label=u'Grados', 
        queryset=Grado.objects.all()
    )
    horas = forms.ModelChoiceField(
        label=u'Horas', 
        queryset=horas.objects.all()
    )
    materia = forms.ModelChoiceField(
        label=u'Materia', 
        queryset=Asignacion_Materia.objects.all()
    )

    def __init__(self, *args, **kwargs):
        super(GradonivelForm, self).__init__(*args, **kwargs)
        self.fields['grado'].queryset = Municipio.objects.none()
        self.fields['horas'].queryset = Localidad.objects.none()

Secciones = [
    ('A', 'A'),
    ('B', 'B'),
]

class GradoCursosForm(forms.Form):
    Grado = forms.ModelChoiceField(
        label=u'Grado', 
        queryset=Grado.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control custom-select-value'}),
    )
    Seccion = forms.MultipleChoiceField(
        required=False,
        widget=forms.Select(attrs={'class': 'form-control custom-select-value'}),
        choices=Secciones,
    )
    Materias = forms.ModelChoiceField(
        label=u'Materias', 
        queryset=Asignacion_Materia.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control custom-select-value'}),
    )
    contenido = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class': 'form-control'}))
    pagina = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(GradoCursosForm, self).__init__(*args, **kwargs)
        self.fields['Materias'].queryset = Asignacion_Materia.objects.none()

class ContenidoExamenForm(forms.ModelForm):

    class Meta:
        model = ContenidoExamen
        fields = ('asignacion_materias','Seccion','contenido','pagina')
        widgets = {
            'asignacion_materias': forms.TextInput(attrs={'class': 'form-control'}),
            'Seccion': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.TextInput(attrs={'class': 'form-control'}),
            'pagina': forms.TextInput(attrs={'class': 'form-control'}),
              }  
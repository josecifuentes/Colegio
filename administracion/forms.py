from django import forms
from .models import Alumno, Grado, Pago, Papeleria
from .models import Encargado, Examene
from .models import Encargados_alumnos
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

class AlumnoForm(forms.ModelForm):

    class Meta:
        model = Alumno
        fields = ('Codigo', 'Primer_Nombre', 'Segundo_Nombre', 'Tercer_Nombre', 'Primer_Apellido', 'Segundo_Apellido', 'Grado','Seccion', 'Genero', 'nacimiento', 'direccion', 'telefono', 'estado')
        widgets = {
        	'Codigo': forms.TextInput(attrs={'class': 'form-control','data-mask': '9999-999','placeholder': 'Máximo 7 dígitos...'}),
  			'Primer_Nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba El Primer Nombre Del Alumno'}),
 			'Segundo_Nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba El Segundo Nombre Del Alumno'}),
 			'Tercer_Nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba El Tercer Nombre Del Alumno'}),
 			'Primer_Apellido': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba El Primer Apellido Del Alumno'}),
 			'Segundo_Apellido': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba El Segundo Apellido Del Alumno'}),
 			'Grado': forms.Select(attrs={'class': 'chosen-select','data-placeholder': 'Seleccione Un Grado...'}),
 			'Seccion': forms.Select(attrs={'class': 'form-control custom-select-value'}),
 			'Genero': forms.Select(attrs={'class': 'form-control custom-select-value'}),
 			'nacimiento': forms.TextInput(attrs={'class': 'form-control','value': '01/01/2000'}),
			'direccion': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba La Direccion Del Alumno'}),
 			'telefono': forms.TextInput(attrs={'class': 'form-control','data-mask': '9999-9999','placeholder': 'Máximo 8 dígitos...'}),
  			'estado': forms.Select(attrs={'class': 'form-control custom-select-value'}),
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
        fields = ('Alumno','Boleta','Comentario','Estado_Examen')
        widgets = {
            'Alumno': forms.Select(attrs={'class': 'chosen-select','data-placeholder': 'Seleccione Un Alumno...'}),
            'Boleta': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba La Boleta De Pago Del Alumno'}),
            'Comentario': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Comentario Al Pago Del Alumno'}),
            'Estado_Examen': forms.Select(attrs={'class': 'chosen-select','data-placeholder': 'Seleccione El Pago...'}),
        }  

class MyForm(forms.Form): #Notar que no hereda de forms.ModelForm
    
    codigo = forms.CharField()

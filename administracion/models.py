from django.db import models
from django.contrib import admin
from django.core.validators import MaxValueValidator, MinValueValidator

#alumnos
class Aula(models.Model):
    Nombre_Aula  =   models.CharField(max_length=130)
    Numero_Alumnos = models.IntegerField()
    Fecha_Ingreso = models.DateTimeField(blank=True, null=True)
    Estados = (
	    ('Activo', 'Activo'),
	    ('Inactivo', 'Inactivo'),
	    )
    Estado = models.CharField(
	    max_length=10,
	    choices=Estados,
	    default='Activo',
	    )
    def publish(self):
    	self.Fecha_Ingreso = timezone.now()
    	self.save()

    def __str__(self):
        return self.Nombre_Aula

class Grado(models.Model):
    Nombre_Grado  =   models.CharField(max_length=130)
    Aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    Niveles = (
	    ('Pre-Primaria','Pre-Primaria'),
	    ('Primaria', 'Primaria'),
	    ('Basico', 'Basico'),
	    ('Diversificado', 'Diversificado'),
	        )
    Nivel = models.CharField(
	    max_length=100,
	    choices=Niveles,
	    default='Pre-Primaria',
	    )
    Estados = (
	    ('Activo', 'Activo'),
	    ('Inactivo', 'Inactivo'),
	    )
    Estado = models.CharField(
	    max_length=10,
	    choices=Estados,
	    default='Activo',
	    )
    Fecha_Ingreso = models.DateTimeField(blank=True, null=True)
	
    def publish(self):
    	self.Fecha_Ingreso = timezone.now()
    	self.save()

    def __str__(self):
        return '%s %s' % (self.Nombre_Grado, self.Nivel)

class Materia(models.Model):
    Nombre_Materia  =   models.CharField(max_length=130)
    Estados = (
	    ('Activo', 'Activo'),
	    ('Inactivo', 'Inactivo'),
	    )
    Estado = models.CharField(
	    max_length=10,
	    choices=Estados,
	    default='Activo',
	    )
    Fecha_Ingreso = models.DateTimeField(blank=True, null=True)
	
    def publish(self):
    	self.Fecha_Ingreso = timezone.now()
    	self.save()

    def __str__(self):
        return '%s' % (self.Nombre_Materia)

class Alumno(models.Model):
    Creado = models.ForeignKey('auth.User', on_delete=models.CASCADE,blank=True, null=True)
    Codigo = models.CharField(max_length=200,null=True,blank=True)
    Primer_Nombre = models.CharField(max_length=200,)
    Segundo_Nombre = models.CharField(max_length=200, blank=True, null=True)
    Tercer_Nombre = models.CharField(max_length=200,null=True,blank=True)
    Primer_Apellido = models.CharField(max_length=200,blank=True, null=True)
    Segundo_Apellido = models.CharField(max_length=200,blank=True, null=True)
    Grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    SECCIONES = (
        ('A', 'A'),
        ('B', 'B'),
    )
    Seccion = models.CharField(
        max_length=7,
        choices=SECCIONES,
        default='A',
    )
    HOMBRE = 'Hombre'
    MUJER = 'Mujer'
    GENEROS = (
        (HOMBRE, 'Hombre'),
        (MUJER, 'Mujer'),
    )
    Genero = models.CharField(
        max_length=7,
        choices=GENEROS,
        default=HOMBRE,
    )
    nacimiento = models.DateField(
           blank=False, null=False)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=200, blank=True, null=True)
    Estados = (
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo'),
    ('PendienteExamen', 'Pendiente De Examen'),
    ('PendienteInscripcion', 'Pendiente De Inscripcion'),
    )
    estado = models.CharField(
        max_length=20,
        choices=Estados,
        default='Inactivo',
    )
    fechaingreso = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.fechaingreso = timezone.now()
        self.save()

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.Codigo,self.Primer_Nombre, self.Segundo_Nombre, self.Primer_Apellido, self.Segundo_Apellido, self.Grado)

class Encargado(models.Model):
    Nombres = models.CharField(max_length=200)
    Apellidos = models.CharField(max_length=200)
    telefono_celular = models.CharField(max_length=200, blank=True, null=True)
    direccion = models.CharField(max_length=200)
    telefono_casa = models.CharField(max_length=200, blank=True, null=True)
    Trabajo = models.CharField(max_length=200, blank=True, null=True)
    telefono_trabajo = models.CharField(max_length=200, blank=True, null=True)
    Dpi = models.CharField(max_length=200, blank=True, null=True)
    Estados = (
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo'),
    )
    estado = models.CharField(
        max_length=20,
        choices=Estados,
        default='Inactivo',
    )
    fechaingreso = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.fechaingreso = timezone.now()
        self.save()

    def __str__(self):
        return '%s %s' % (self.Nombres, self.Apellidos)

class Examene(models.Model):
    Alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    Boleta = models.CharField(max_length=200)
    Estados = (
    ('Pendiente', 'Pendiente'),
    ('Aprobado', 'Aprobado'),
    ('Reprobado', 'Reprobado'),
    )
    Comentario = models.CharField(max_length=200, blank=True, null=True)
    Estado_Examen = models.CharField(
        max_length=20,
        choices=Estados,
        default='Pendiente',
    )
    fechaingreso = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.fechaingreso = timezone.now()
        self.save()
    def __str__(self):
        return '%s %s %s' % (self.Boleta, self.Alumno, self.Estado_Examen)
   

class Pago(models.Model):
    Alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    Boleta = models.CharField(max_length=200)
    Cantidad = models.CharField(max_length=10, blank=True, null=True)
    Tipos = (
    ('Examen', 'Examen'),
    ('Seguro', 'Seguro'),
    ('Inscripcion', 'Inscripcion'),
    ('Enero', 'Enero'),
    ('Febrero', 'Febrero'),
    ('Marzo', 'Marzo'),
    ('Abril', 'Abril'),
    ('Mayo', 'Mayo'),
    ('Junio', 'Junio'),
    ('Julio', 'Julio'),
    ('Agosto', 'Agosto'),
    ('Septiembre', 'Septiembre'),
    ('Octubre', 'Octubre'),
    ('Otro', 'Otro'),
    )
    Comentario = models.CharField(max_length=200, blank=True, null=True)
    Tipo_Pago = models.CharField(
        max_length=20,
        choices=Tipos,
        default='Inscripcion',
    )
    
    def __str__(self):
        return '%s %s %s' % (self.Boleta, self.Alumno, self.Tipo_Pago)
    class Meta:
        unique_together = (("Alumno", "Tipo_Pago"),)

class Papeleria(models.Model):
    Alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE)
    Padre = models.ForeignKey(Encargado, on_delete=models.CASCADE, blank=True, null=True, related_name='Padre')
    Madre = models.ForeignKey(Encargado, on_delete=models.CASCADE, blank=True, null=True, related_name='Madre')
    Alergias = models.CharField(max_length=200, blank=True, null=True)
    Enfermedades = models.CharField(max_length=200, blank=True, null=True)
    Nombre_Doctor = models.CharField(max_length=200, blank=True, null=True)
    Telefono_Doctor = models.CharField(max_length=200, blank=True, null=True)
    Cui = models.CharField(max_length=200, blank=True, null=True)
    Tipos = (
    ('Recibido', 'Recibido'),
    ('No_Entregado', 'No Entregado'),
    ('No_Cuenta_Con', 'No Cuenta Con'),
    )
    Partida_Nacimiento = models.CharField(
        max_length=30,
        choices=Tipos,
        default='No_Entregado',
    )
    Certificado_Pre_Primaria = models.CharField(
        max_length=30,
        choices=Tipos,
        default='No_Entregado',
    )
    Certificado_Primaria = models.CharField(
        max_length=30,
        choices=Tipos,
        default='No_Entregado',
    )
    Certificado_Basico = models.CharField(
        max_length=30,
        choices=Tipos,
        default='No_Entregado',
    )
    Certificado_Bachillerato = models.CharField(
        max_length=30,
        choices=Tipos,
        default='No_Entregado',
    )
    Sangre = (
    ('Desconocido', 'Desconocido'),
    ('O_negativo', 'O negativo'),
    ('O_positivo', 'O positivoo'),
    ('A_negativo', 'A negativo'),
    ('A_positivo', 'A positivo'),
    ('B_negativo', 'B negativo'),
    ('B_positivo', 'B positivo'),
    ('AB_negativo', 'AB negativo'),
    ('AB_positivo', 'AB positivo'),
    )
    Tipo_Sangre = models.CharField(
        max_length=30,
        choices=Sangre,
        default='Desconocido',
        blank=True, 
        null=True,
    )
    Comentarios = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return '%s %s %s' % (self.Boleta, self.Alumno, self.Tipo_Pago)

class Personal(models.Model):
    Primer_Nombre = models.CharField(max_length=200)
    Segundo_Nombre = models.CharField(max_length=200, default='N/A')
    Primer_Apellido = models.CharField(max_length=200)
    Segundo_Apellido = models.CharField(max_length=200, default='N/A')
    Telefono_Casa = models.CharField(max_length=200, blank=True, null=True)
    Telefono_Celular = models.CharField(max_length=200, blank=True, null=True)
    Direccion = models.CharField(max_length=128)
    Dpi = models.CharField(max_length=20)
    Tipos = (
    ('Soltero', 'Soltero'),
    ('Casado', 'Casado'),
    ('Viudo', 'Viudo'),
    ('Divorsiado', 'Divorsiado'),
    )
    Estado_Civil = models.CharField(
        max_length=20,
        choices=Tipos,
        default='Soltero',
    )
    Fecha_Nacimiento = models.DateField(
        blank=True, null=True)
    Lugar_Nacimiento = models.CharField(max_length=128)
    hijos = (
    ('sin', 'Sin Hijos'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('mas', 'Mas de 5...'),
    )
    No_Hijos= models.CharField(
        max_length=20,
        choices=hijos,
        default='sin',
    )
    Nit = models.CharField(max_length=20)
    Igss = models.CharField(max_length=30)
    Fecha_Inicio_Labores = models.DateField(
        blank=True, null=True)
    Nivel_Academico = models.CharField(max_length=50)
    Titulo = models.CharField(max_length=50)
    Cedula_Docente = models.CharField(max_length=50)
    Registro_Escalafonario = models.CharField(max_length=50)
    Salario = models.CharField(max_length=50)
    Hora_Entrada = models.TimeField(blank=True, null=True)
    Hora_Salida = models.TimeField(blank=True, null=True)
    fechaingreso = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.fechaingreso = timezone.now()
        self.save()

    def __str__(self):
        return '%s %s' % (self.Primer_Nombre, self.Primer_Apellido)
  
class Asignacion_Materia (models.Model):

    Grado = models.ForeignKey(Grado, on_delete=models.CASCADE)

    Materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

    Personal  = models.ForeignKey(Personal, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.Grado, self.Materia, self.Personal)
    class Meta:
        unique_together = (("Grado", "Materia"),)

class Asignacion_Acividade (models.Model):

    Asignacion_Materia = models.ForeignKey(Asignacion_Materia, on_delete=models.CASCADE)
    Unidades = (
    ('uni1', 'Primera Unidad'),
    ('uni2', 'Segunda Unidad'),
    ('uni3', 'Tercera Unidad'),
    ('uni4', 'Cuarta Unidad'),
    )
    Unidad = models.CharField(
        max_length=20,
        choices=Unidades,
        default='Primera Unidad',
    )
    Tipos = (
    ('Act1', 'Actividad 1'),
    ('Act2', 'Actividad 2'),
    ('Act3', 'Actividad 3'),
    ('Act4', 'Actividad 4'),
    ('Act5', 'Actividad 5'),
    ('Act6', 'Actividad 6'),
    ('Act7', 'Actividad 7'),
    ('Act8', 'Actividad 8'),
    ('Act9', 'Actividad 9'),
    ('Act10', 'Actividad 10'),
    ('Exa', 'Examen Final'),
    )
    Nombre_Actividad = models.CharField(
        max_length=20,
        choices=Tipos,
        default='Actividad 1',
    )
    Descripcion_Actividad =  models.CharField(max_length=200)
    Ponderacion = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(60),
            MinValueValidator(1)
        ]
     )

    def __str__(self):
        return '%s %s' % (self.Asignacion_Materia, self.Ponderacion)

class Asignacion_MateriaInLine(admin.TabularInline):

    model = Asignacion_Materia

#muestra un campo extra al momento de insertar, como indicación que se pueden ingresar N actores.

    extra = 1

class GradoAdmin(admin.ModelAdmin):

    inlines = (Asignacion_MateriaInLine,)

class MateriaAdmin (admin.ModelAdmin):

    inlines = (Asignacion_MateriaInLine,)

class Encargados_alumnos (models.Model):

    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    encargado = models.ForeignKey(Encargado, on_delete=models.CASCADE)
    parentesco = models.CharField(max_length=130,blank=True, null=True)


class Encargados_alumnosInLine(admin.TabularInline):

    model = Encargados_alumnos

#muestra un campo extra al momento de insertar, como indicación que se pueden ingresar N actores.

    extra = 1


class AlumnoAdmin(admin.ModelAdmin):

    inlines = (Encargados_alumnosInLine,)


class EncargadoAdmin (admin.ModelAdmin):

    inlines = (Encargados_alumnosInLine,)
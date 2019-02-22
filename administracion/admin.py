from django.contrib import admin
from administracion.models import Asignacion_Punteo,Asignacion_Grado,Asignacion_Permiso,Permiso,Aula, Grado, Materia, GradoAdmin, MateriaAdmin, Alumno, Encargado, EncargadoAdmin, AlumnoAdmin, Examene, Pago, Papeleria, Personal, Asignacion_Materia, Asignacion_Acividade,Actividade

#Registramos nuestras clases principales.
admin.site.register(Aula)
admin.site.register(Grado, GradoAdmin)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Encargado, EncargadoAdmin)
admin.site.register(Examene)
admin.site.register(Pago)
admin.site.register(Papeleria)
admin.site.register(Personal)
admin.site.register(Asignacion_Materia)
admin.site.register(Asignacion_Acividade)
admin.site.register(Actividade)
admin.site.register(Permiso)
admin.site.register(Asignacion_Permiso)
admin.site.register(Asignacion_Grado)
admin.site.register(Asignacion_Punteo)
from django.contrib import admin
from administracion.models import Aula, Grado, Materia, GradoAdmin, MateriaAdmin, Alumno, Encargado, EncargadoAdmin, AlumnoAdmin, Examene, Pago, Papeleria, Personal, Asignacion_Materia, Asignacion_Acividade

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

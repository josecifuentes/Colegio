from django.contrib import admin
from administracion.models import Reportes,ContenidoExamen,HorarioExamen,Periodo,horas,Asignacion_Punteo,Asignacion_Grado,Asignacion_Permiso,Permiso,Aula, Grado, Materia, GradoAdmin, MateriaAdmin, Alumno, Encargado, EncargadoAdmin, AlumnoAdmin, Examene, Pago, Papeleria, Personal, Asignacion_Materia, Asignacion_Acividade,Actividade



class AlumnoAdmin(admin.ModelAdmin):
    # con esto añades un campo de texto que te permite realizar la busqueda, puedes añadir mas de un atributo por el cual se filtrará
    search_fields = ['Primer_Nombre', 'Primer_Apellido','Codigo']
    # con esto añadiras una lista desplegable con la que podras filtrar (activo es un atributo booleano)
    list_filter = ['Primer_Nombre']

class Asignacion_PermisoAdmin(admin.ModelAdmin):
    # con esto añades un campo de texto que te permite realizar la busqueda, puedes añadir mas de un atributo por el cual se filtrará
    search_fields = ['Usuario__username','Permiso__Nombre']
    # con esto añadiras una lista desplegable con la que podras filtrar (activo es un atributo booleano)
    list_filter = ['Usuario']
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
admin.site.register(Asignacion_Permiso,Asignacion_PermisoAdmin)
admin.site.register(Asignacion_Grado)
admin.site.register(Asignacion_Punteo)
admin.site.register(horas)
admin.site.register(Periodo)
admin.site.register(HorarioExamen)
admin.site.register(ContenidoExamen)
admin.site.register(Reportes)

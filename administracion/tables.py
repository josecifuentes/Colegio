from .models import Alumno, Grado, Pago, Papeleria,Asignacion_Acividade,Asignacion_Punteo

 
class Asignacion_PunteoTable(Table):
    Alumno = Column(field='Alumno', header=u'Alumno')
    Asignacion_Acividades = Column(field='Asignacion_Acividades', header=u'Asignacion_Acividades.Nombre')
    Nota = Column(field='Nota', header=u'Nota')
    class Meta:
        model = Asignacion_Punteo

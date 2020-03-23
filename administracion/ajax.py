from django.http import JsonResponse
from .models import Asignacion_Materia,Grado


def get_materias(request):
    grado_id = request.GET.get('grado_id')
    seccion = request.GET.get('seccion')
    print(seccion)
    materias = Asignacion_Materia.objects.none()
    options = '<option value="" selected="selected">---------</option>'
    if grado_id:
        materias = Asignacion_Materia.objects.filter(Grado_id=grado_id,Seccion=seccion)   
    for materia in materias:
        options += '<option value="%s">%s</option>' % (
            materia.pk,
            materia.Materia
        )
    response = {}
    response['materias'] = options
    return JsonResponse(response)

def get_grados(request):
    nivel = request.GET.get('nivelid')

    grados = Grado.objects.none()
    options = '<option value="" selected="Seleccione un grado">---------</option>'
    if nivel:
        grados = Grado.objects.filter(Nivel=nivel)   
        print(grados)
    for grado in grados:
        options += '<option value="%s">%s</option>' % (
            grado.pk,
            grado
        )
    response = {}
    response['grados'] = options
    return JsonResponse(response)

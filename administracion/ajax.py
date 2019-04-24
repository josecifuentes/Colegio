from django.http import JsonResponse

from .models import Grado, horas


def get_grados(request):
    grado_id = request.GET.get('grado_id')
    grados = Grado.objects.none()
    options = '<option value="" selected="selected">---------</option>'
    if grado_id:
        grados = Grado.objects.filter(pk=grado_id)   
    for grado in grados:
        options += '<option value="%s">%s</option>' % (
            grado.pk,
            grado.Nombre_Grado
        )
    response = {}
    response['grados'] = options
    return JsonResponse(response)


def get_localidades(request):
    municipio_id = request.GET.get('municipio_id')
    localidades = Localidad.objects.none()
    options = '<option value="" selected="selected">---------</option>'
    if municipio_id:
        localidades = Localidad.objects.filter(municipio_id=municipio_id)   
    for localidad in localidades:
        options += '<option value="%s">%s</option>' % (
            localidad.pk,
            localidad.localidad
        )
    response = {}
    response['localidades'] = options
    return JsonResponse(response)
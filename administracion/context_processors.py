from .models import Asignacion_Permiso 
def data_templates(request):
	asignado = []
	try:
		permiso = Asignacion_Permiso.objects.filter(Usuario = request.user)
		for perm in permiso:
			if(perm.Estado == "Activo"):
				asignado.append(perm.Permiso)
	except Exception as e:
		permiso = None
		asignado = None
	return {'Permisos': asignado}
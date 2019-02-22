from django import template
register = template.Library()

@register.filter
def index(List, i):
    return List[i]
@register.filter 
def actividad(value):
	if value == "Act1":
		data="Actividad 1"
	if value == "Act2":
		data="Actividad 2"
	if value == "Act3":
		data="Actividad 3"
	if value == "Act4":
		data="Actividad 4"
	if value == "Act5":
		data="Actividad 5"
	if value == "Act6":
		data="Actividad 6"
	if value == "Act7":
		data="Actividad 7"
	if value == "Act8":
		data="Actividad 8"
	if value == "Act9":
		data="Actividad 9"
	if value == "Act10":
		data="Actividad 10"
	return data    
@register.filter 
def mes(value):
	data= "Enero"
	if int(value) == 1:
		data="Enero"
	if int(value) == 2:
		data="Febrero"
	if int(value) == 3:
		data="Marzo"
	if int(value) == 4:
		data="Abril"
	if int(value) == 5:
		data="Mayo"
	if int(value) == 6:
		data="Junio"
	if int(value) == 7:
		data="Julio"
	if int(value) == 8:
		data="Agosto"
	if int(value) == 9:
		data="Septiembre"
	if int(value) == 10:
		data="Octubre"
	if int(value) == 11:
		data="Noviembre"
	if int(value) == 12:
		data="Diciembre"
	return data 

@register.filter 
def meses(value):
	data= "Ene"
	if int(value) == 1:
		data="Ene"
	if int(value) == 2:
		data="Feb"
	if int(value) == 3:
		data="Mar"
	if int(value) == 4:
		data="Abr"
	if int(value) == 5:
		data="May"
	if int(value) == 6:
		data="Jun"
	if int(value) == 7:
		data="Jul"
	if int(value) == 8:
		data="Ago"
	if int(value) == 9:
		data="Sep"
	if int(value) == 10:
		data="Oct"
	if int(value) == 11:
		data="Nov"
	if int(value) == 12:
		data="Dic"
	return data

@register.filter 
def buscar(value):
	if value == "uni1":
		data="Primera Unidad"
	if value == "uni2":
		data="Segunda Unidad"
	if value == "uni3":
		data="Tercera Unidad"
	if value == "uni4":
		data="Cuarta Unidad"
	return data
@register.filter
def porcentaje(valor):
	data= "0"
	if int(valor) < 5 and int(valor) > 0:
		data = "1/8"
	if int(valor) < 10 and int(valor) >= 5:
		data = "1/6"
	if int(valor) < 20 and int(valor) >= 10:
		data = "1/4"
	if int(valor) < 40 and int(valor) >= 20:
		data = "1/2"
	if int(valor) == 40: 
		data="1/2"
	return data
    
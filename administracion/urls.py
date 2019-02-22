from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path, include

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('alumno/<int:pk>/', views.alumno_editar, name='alumno_editar'),
    path('encargado/asignacion/nuevo/', views.nueva_asignacion_encargado, name='nueva_asignacion_encargado'),
    path('encargado/<int:pk>/', views.encargado, name='encargado'),
    path('pagos/asignacion/', views.asignacion_pagos, name='asignacion_pagos'),
    path('alumno/nuevo/', views.nuevo_alumno, name='nuevo_alumno'),
    path('alumno/agregar_papeleria/<int:pk>/', views.agregar_papeleria, name='agregar_papeleria'),
    path('alumno/asignacion/<int:pk>', views.asignacion_alumno, name='asignacion_alumno'),
    path('encargado/ver/', views.ver_encargados, name='ver_encargados'),
    path('pagos/ver/', views.ver_pagos, name='ver_pagos'),
    path('examenes/ver/', views.ver_examenes, name='ver_examenes'),
    path('examenes/asignacion/', views.agregar_examenes, name='agregar_examenes'),
    path('encargado/nuevo/', views.nuevo_encargado, name='nuevo_encargado'),
    path('encargado/asignacion/<int:pk>', views.asignacion_encargado, name='asignacion_encargado'),
    path('alumno/buscar', views.buscar_papeleria, name='buscar_papeleria'),
    path('alumno/papeleria/<int:pk>', views.papelerias, name='papeleria'),
    path('cerrarsession/', views.cerrar, name='cerrar'),
    path('alumno/error/', views.error, name='error'),
    path('examenes/error/', views.no_pago, name='no_pago'),
    path('calendario/', views.calendario, name='calendario'),
    path('calendario/<int:pk>', views.calendario_info, name='calendario_info'),
    path('horario/', views.horario, name='horario'),
    path('horarios/', views.horarios, name='horarios'),
    path('horas/', views.horas, name='horas'),
    path('horarios/grado', views.horarios_grado, name='horarios_grado'),
    path('perfil/', views.perfil, name='perfil'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('Notas/', views.notas, name='notas'),
    path('asignacion/notas/<int:pk>', views.asignacion_notas, name='asignacion_notas'),
    path('actividades/', views.actividades_cursos, name='actividades_cursos'),
    path('asignacion/actividades/<int:pk>', views.asignacion_actividades, name='asignacion_actividades'),
    path('actividades/nuevo/<int:pk>', views.nueva_actividad, name='nueva_actividad'),
    path('actividades/eliminar/<int:pk>', views.eliminar_actividad, name='eliminar_actividad'),
    path('notas/actualizar/<int:pk>', views.estado_nota, name='estado_nota'),
    path('asignacion/notas/ponderar/', views.ponderar, name='ponderar'),
    path('asignacion/permisos/', views.asignar_permisos, name='asignar_permisos'),
    path('asignacion/permisos/asignar/<int:pk>', views.listado_permisos, name='listado_permisos'),

    
]
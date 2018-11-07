from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('alumno/<int:pk>/', views.estudiante, name='estudiante'),
    path('alumno/nuevo/', views.nuevo_alumno, name='nuevo_alumno'),
    path('encargado/nuevo/', views.nuevo_encargado, name='nuevo_encargado'),
    path('encargado/asignacion/', views.asignacion_encargado, name='asignacion_encargado'),
]
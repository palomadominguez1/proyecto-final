from django.urls import path
from app_coder import views
from .views import redirect_view

urlpatterns = [
    # path('inicio', views.inicio),
    path('cursos', views.cursos, name="Cursos"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('profesor', views.profesor, name="Profesor"),
    path('inicio', views.index, name="Inicio"),
    # path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    # path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    path('busquedaCurso', views.busquedaCurso, name="BusquedaCurso"),
    path('buscar/', views.buscar)
]
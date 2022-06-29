from django.urls import path
from app_coder import views
from .views import redirect_view
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cursos', views.cursos, name="Cursos"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('profesor', views.profesor, name="Profesor"),
    path('inicio', views.index, name="Inicio"),
    path('busquedaCurso', views.busquedaCurso, name="BusquedaCurso"),
    path('buscar/', views.buscar),
    path('curso/list', views.CursoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'),
    path('curso/nuevo', views.CursoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),
    path('app_coder/login', views.login_request, name='Login'),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='app_coder/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('profesor/list', views.ProfeList.as_view(), name='ProfeList'),
    path('estudiantes/list', views.EstudianteList.as_view(), name='EstudianteList'),
    path('sobre_mi', views.aboutme, name='SobreMi')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
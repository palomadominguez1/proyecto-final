import email
from django.shortcuts import render
from app_coder.models import Curso
from app_coder.models import Estudiante
from app_coder.models import Profesor
from django.http import HttpResponse

from app_coder.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario
# Create your views here.


# def cursos(request):
#     return render(request, "app_coder/cursos.html")
from django.shortcuts import redirect

def redirect_view(request):
    response = redirect('/app_coder/inicio')
    return response

def estudiantes(request):
    if request.method == "POST":
        miFormulario = EstudianteFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            estudiante = Estudiante(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            estudiante.save()
            miFormulario = EstudianteFormulario()
            return render(request, "app_coder/estudiantes.html", {"miFormulario":miFormulario})
    else:
        miFormulario = EstudianteFormulario()

    return render(request, "app_coder/estudiantes.html", {"miFormulario":miFormulario})



# def profesor(request):
#     return render(request, "app_coder/profesor.html")


def inicio(request):
    return render(request, "app_coder/index.html")


def index(request):
    return render(request, "app_coder/index.html")


def cursos(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])
            curso.save()
            miFormulario = CursoFormulario()
            return render(request, "app_coder/cursos.html", {"miFormulario":miFormulario})
    else:
        miFormulario = CursoFormulario()

    return render(request, "app_coder/cursos.html", {"miFormulario":miFormulario})

def profesor(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])
            profesor.save()
            miFormulario = ProfesorFormulario()
            return render(request, "app_coder/profesor.html", {"miFormulario":miFormulario})
    else:
        miFormulario = ProfesorFormulario()
        return render(request, "app_coder/profesor.html", {"miFormulario":miFormulario})


def busquedaCurso(request):
    return render(request, 'app_coder/busquedaCurso.html')

def buscar(request):
    if request.GET['camada']:
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(request, "app_coder/busquedaCurso.html", {"cursos":cursos, "camada":camada})

    else: 
        respuesta = "No enviaste datos"

    # respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
    # return HttpResponse(respuesta)
    return render(request, "app_coder/busquedaCurso.html", {"respuesta":respuesta})

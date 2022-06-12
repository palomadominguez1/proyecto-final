import email
from django.shortcuts import render
from app_coder.models import Curso
from app_coder.models import Estudiante
from app_coder.models import Profesor
from django.http import HttpResponse

from app_coder.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario, UserRegistrationForm, UserEditForm
# Create your views here.
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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

@login_required
def inicio(request):
    return render(request, "app_coder/index.html")

@login_required
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



class CursoList(ListView):
    model = Curso
    template_name = "app_coder/cursos_list.html"

class CursoDetalle(DetailView):
    model = Curso
    template_name = "app_coder/curso_detalle.html"

class CursoCreacion(CreateView):
    model = Curso
    success_url = "/app_coder/curso/list"
    fields = ['nombre', 'camada']

class CursoUpdate(UpdateView):
    model = Curso
    success_url = "/app_coder/curso/list"
    fields = ['nombre', 'camada']

class CursoDelete(DeleteView):
    model = Curso
    success_url = "/app_coder/curso/list"


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return render(request, 'app_coder/index.html', {"mensaje":f"Bienvenido {usuario}"})
            else: 
                return render(request, 'app_coder/index.html', {"mensaje":"Error, datos incorrectos"})
        else: 
            return render(request, 'app_coder/index.html', {"mensaje":"Error, datos incorrectos"})
        
    form = AuthenticationForm()

    return render(request, 'app_coder/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "app_coder/index.html", {"mensaje": f"Usuario {username} Creado con éxito"})

    else:
        form = UserRegistrationForm()

    return render(request, "app_coder/registro.html", {"form":form})

@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.save()

            return render(request, 'app_coder/index.html')

    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render(request, 'app_coder/editarPerfil.html', {'miFormulario':miFormulario, 'usuario':usuario})
            
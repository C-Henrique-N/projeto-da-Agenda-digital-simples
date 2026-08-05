from django.shortcuts import render, redirect
from .models import Tarefa
from .forms import TarefaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import TarefaForm, CadastroForm
from django.contrib.auth import login

@login_required
def home(request):
    if request.method == "POST":
        form = TarefaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TarefaForm()

    filtro = request.GET.get('status')

    if filtro == "pendentes": 
        tarefas = Tarefa.objects.filter(concluida=False).order_by('data', 'horario')
    elif filtro == "concluidas":
        tarefas = Tarefa.objects.filter(concluida=True).order_by('data', 'horario')
    else:
        tarefas = Tarefa.objects.order_by('data', 'horario')

    return render(request, "tarefas/home.html", {"tarefas": tarefas, "form": form})

def excluir_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    tarefa.delete() 
    return redirect("home")

def concluir_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    tarefa.concluida = True 
    tarefa.save()
    return redirect("home")

def editar_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)

    if request.method == "POST":
        form = TarefaForm(request.POST, instance=tarefa)

        if form.is_valid(): 
            form.save()
            return redirect("home")
    
    else:
        form = TarefaForm(instance=tarefa)
    
    return render(request, "tarefas/home.html", {"form": form, "tarefas": Tarefa.objects.all()    })

class LoginUsuario(LoginView):
    template_name = "tarefas/login.html"
    redirect_authenticated_user = True
    
def cadastro(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CadastroForm()

    return render(request, "tarefas/cadastro.html", {"form": form})
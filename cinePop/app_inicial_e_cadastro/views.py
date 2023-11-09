from django.shortcuts import render
from .models import Usuario
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView

def home(request):
    return render(request,'paginaInicial/home.html')

def cadastro(request):
    if request.method == "GET":
        return render(request,'cadastroUsuarios/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse(f'Já existe um usuário com esse username {username}')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return HttpResponse(f'Usuário {username} cadastrado e autenticado com sucesso.')

class CustomLoginView(LoginView):
    template_name = 'paginaInicial/home.html'

def login(request):
    if request.method == "GET":
        return render(request, 'login/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            return HttpResponse('Autenticado')
        else:
            return HttpResponse('Usuário ou senha errados')

def usuarios(request):
    # Salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.save()
    # Exibir todos os usuários já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    # Retornar os dados para a página de listagem de usuários
    return render(request, 'adm/listagem_usuarios.html',usuarios)

def listagem_usuarios(request):
    return render(request, 'adm/listagem_usuarios.html')


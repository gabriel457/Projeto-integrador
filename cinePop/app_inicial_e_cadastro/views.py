from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'paginaInicial/home.html')

def cadastro(request):
    return render(request,'cadastroUsuarios/cadastro.html')

def login(request):
    return render(request, 'login/login.html')

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


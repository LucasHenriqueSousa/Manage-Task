from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from .forms import SignUpForm

# View responsável pela página inicial e autenticação do usuário
def home(request):
    """
    View para a página inicial e login do usuário.
    
    Se o método da requisição for POST, tenta autenticar o usuário com as credenciais fornecidas.
    - Se a autenticação for bem-sucedida, o usuário é logado e uma mensagem de sucesso é exibida.
    - Se a autenticação falhar, exibe uma mensagem de erro.
    
    Args:
        request: Objeto HttpRequest contendo dados da requisição.
    
    Returns:
        HttpResponse: Redireciona para a página inicial se o login for bem-sucedido.
                      Renderiza a página 'home.html' com mensagens de feedback sobre o login.
    """
    if request.method == 'POST':
        # Obtém o nome de usuário e senha do formulário de login
        username = request.POST['usuario']
        password = request.POST['senha']
        
        # Autentica o usuário com as credenciais fornecidas
        user = authenticate(request, username=username, password=password)
        
        # Se a autenticação for bem-sucedida, realiza o login e exibe uma mensagem de sucesso
        if user is not None:
            login(request, user)
            messages.success(request, 'Login foi realizado com sucesso!')
            return redirect('home')
        
        # Se a autenticação falhar, exibe uma mensagem de erro
        else:
            messages.error(request, 'Erro na autenticação. Tente novamente!')
            return redirect('home')
    else:    
        return render(request, 'home.html')

# View responsável pelo logout do usuário
def logout_user(request):
    """
    View para realizar o logout do usuário.
    
    Encerra a sessão do usuário e exibe uma mensagem de sucesso.
    
    Args:
        request: Objeto HttpRequest contendo dados da requisição.
    
    Returns:
        HttpResponse: Redireciona para a página inicial após o logout.
    """
    logout(request)
    messages.success(request, 'Você fez o logout com sucesso!')
    return redirect("home")

# View responsável pelo registro de um novo usuário
def register_user(request):
    """
    View para o registro de um novo usuário.
    
    Se o método da requisição for POST, valida e salva o formulário de registro.
    - Se o formulário for válido, salva o novo usuário no banco de dados, exibe uma mensagem de sucesso
      e redireciona para a página inicial.
    - Se o formulário for inválido, exibe uma mensagem de erro e permanece na página de registro.
    
    Args:
        request: Objeto HttpRequest contendo dados da requisição.
    
    Returns:
        HttpResponse: Redireciona para a página inicial após o registro bem-sucedido.
                      Renderiza a página 'register.html' com o formulário de registro e mensagens de feedback.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o usuário no banco de dados
            messages.success(request, 'Registro realizado com sucesso!')
            return redirect('home')  # Redireciona para a página desejada após o registro
        else:
            messages.error(request, 'Erro ao registrar. Verifique os dados e tente novamente.')
    else:
        form = SignUpForm()
    
    return render(request, 'register.html', {'form': form})


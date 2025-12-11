from django.shortcuts import render, redirect
from .forms import registroform
from .models import Usuario
def registro (request):
    if request.method == 'POST':
        form = registroform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("usuario:lista")
        
    else:
        form = registroform()
    return render(request, 'usuarios/registro.html', {'form':form})

def login(request):
    mensagem = ""

    if request.method == "POST":
        nome = request.POST.get("nome_usuario")
        senha = request.POST.get("senha")

        try:
            usuario = Usuario.objects.filter(nome_usuario=nome).first()

            if usuario.senha == senha:
                return redirect("usuario:lista") 
            else:
                mensagem = "Senha incorreta."

        except Usuario.DoesNotExist:
            mensagem = "Usuário não encontrado."

    return render(request, "usuarios/login.html", {"mensagem": mensagem})

def lista(request):
    usuario = Usuario.objects.all()

    context = {'usuario' : usuario }
    return render(request, 'usuarios/lista.html', context)
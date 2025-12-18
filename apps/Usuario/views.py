from django.shortcuts import render, redirect, get_object_or_404
from .forms import registroform
from .models import Usuario
from apps.Usuario.decorators import admin_required, login_required_custom

def registro (request):
    if request.method == 'POST':
        form = registroform(request.POST, request.FILES)
        if form.is_valid():
            usuario = form.save()
            request.session ['usuario_id'] = usuario.id
            request.session ['usuario_nome'] = usuario.nome_usuario
            request.session ['is_admin'] = usuario.is_admin
            return redirect("jogos:lista")
        
    else:
        form = registroform()
    return render(request, 'usuarios/registro.html', {'form':form, 'titulo': 'Registrar'})

def login(request):
    mensagem = ""

    if request.method == "POST":
        username = request.POST.get("nome_usuario")
        password = request.POST.get("senha")
        usuario = Usuario.objects.filter(nome_usuario=username).first()

        if usuario:
            if usuario.senha == password:
                request.session ['usuario_id'] = usuario.id
                request.session ['usuario_nome'] = usuario.nome_usuario
                request.session ['is_admin'] = usuario.is_admin
                return redirect("jogos:lista")
            else:
                mensagem = "Senha incorreta."
        else:
            mensagem = "Usuário não encontrado."

    return render(request, "usuarios/login.html", {"mensagem": mensagem,"titulo": "Login"})

def logout(request):
    request.session.flush()
    return redirect("usuario:login")

@admin_required
def lista(request):
    usuario = Usuario.objects.all()

    context = {'usuario' : usuario }
    return render(request, 'usuarios/lista.html', context)

def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = registroform(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('genero:lista')
    else:
        form = registroform(instance=usuario)
    return render(request, 'usuarios/registro.html', {'form': form, 'titulo': 'Editar Usuário'})

def excluir_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario:lista')
    return render(request, 'usuarios/excluir.html', {'usuario': usuario})
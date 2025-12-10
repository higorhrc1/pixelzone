# apps/Usuario/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsuarioRegisterForm, UsuarioLoginForm
from .models import Usuario
from pixelzone.utils import hash_password, verify_password, get_logged_user, login_required_custom, admin_required

def registro(request):
    if request.method == 'POST':
        form = UsuarioRegisterForm(request.POST)
        if form.is_valid():
            u = form.save(commit=False)
            u.senha = hash_password(form.cleaned_data['senha'])
            u.save()
            request.session['usuario_id'] = u.id
            return redirect('jogos:lista')
    else:
        form = UsuarioRegisterForm()
    return render(request, 'usuario/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UsuarioLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            try:
                u = Usuario.objects.get(email=email)
            except Usuario.DoesNotExist:
                u = None
            if u and verify_password(senha, u.senha):
                request.session['usuario_id'] = u.id
                return redirect('jogos:lista')
            form.add_error(None, 'Credenciais inválidas.')
    else:
        form = UsuarioLoginForm()
    return render(request, 'usuario/login.html', {'form': form})

def logout_view(request):
    request.session.pop('usuario_id', None)
    return redirect('jogos:lista')

@login_required_custom
def perfil(request):
    usuario = get_logged_user(request)
    return render(request, 'usuario/perfil.html', {'usuario': usuario})

@admin_required
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/lista.html', {'usuarios': usuarios})

@admin_required
def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    from .forms import UsuarioRegisterForm
    if request.method == 'POST':
        form = UsuarioRegisterForm(request.POST, instance=usuario)
        if form.is_valid():
            u = form.save(commit=False)
            if form.cleaned_data.get('senha'):
                u.senha = hash_password(form.cleaned_data['senha'])
            u.save()
            return redirect('usuario:lista')
    else:
        form = UsuarioRegisterForm(instance=usuario)
    return render(request, 'usuario/form.html', {'form': form, 'edit': True})

@admin_required
def excluir_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario:lista')
    return render(request, 'usuario/confirm_delete.html', {'object': usuario})

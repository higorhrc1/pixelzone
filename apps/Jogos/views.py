from django.shortcuts import render, get_object_or_404, redirect
from .models import Jogo
from .forms import JogoForm

# LISTA TODOS OS JOGOS
def lista_jogos(request):
    jogos = Jogo.objects.all()
    return render(request, 'jogos/lista.html', {'jogos': jogos})

# MOSTRA DETALHES DO JOGO
def detalhe_jogo(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    return render(request, 'jogos/detalhe.html', {'jogo': jogo})

# CRIAR NOVO JOGO
def criar_jogo(request):
    if request.method == 'POST':
        form = JogoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jogos:lista')
    else:
        form = JogoForm()
    return render(request, 'jogos/form.html', {'form': form, 'titulo': 'Criar Jogo'})

# EDITAR JOGO
def editar_jogo(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    if request.method == 'POST':
        form = JogoForm(request.POST, instance=jogo)
        if form.is_valid():
            form.save()
            return redirect('detalhe', pk=pk)
    else:
        form = JogoForm(instance=jogo)
    return render(request, 'jogos/form.html', {'form': form, 'titulo': 'Editar Jogo'})

# EXCLUIR JOGO
def excluir_jogo(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    if request.method == 'POST':
        jogo.delete()
        return redirect('jogos:lista')
    return render(request, 'jogos/excluir.html', {'jogo': jogo})

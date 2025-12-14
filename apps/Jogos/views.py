from django.shortcuts import render, get_object_or_404, redirect
from .models import Jogo
from .forms import JogoForm
from apps.Reviews.models import Review

def lista_jogos(request):
    jogos = Jogo.objects.all()
    return render(request, 'jogos/lista.html', {'jogos': jogos})

def detalhe_jogo(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    reviews = Review.objects.filter(jogo=jogo)
    return render(request, 'jogos/detalhe.html', {'jogo': jogo, 'reviews': reviews})

def criar_jogo(request):
    if request.method == 'POST':
        form = JogoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('jogos:lista')
    else:
        form = JogoForm()

    return render(request, 'jogos/form.html', {'form': form,'titulo': 'Criar Jogo'})

def editar_jogo(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)

    if request.method == 'POST':
        form = JogoForm(request.POST, request.FILES, instance=jogo)
        if form.is_valid():
            form.save()
            return redirect('jogos:detalhe', pk=pk)
    else:
        form = JogoForm(instance=jogo)

    return render(request, 'jogos/form.html', {'form': form, 'titulo': 'Editar Jogo'})

def excluir_jogo(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    if request.method == 'POST':
        jogo.delete()
        return redirect('jogos:lista')
    return render(request, 'jogos/excluir.html', {'jogo': jogo})

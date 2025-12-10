from django.shortcuts import render, redirect, get_object_or_404
from .models import Jogo
from .forms import JogoForm
from pixelzone.utils import login_required_custom, admin_required, get_logged_user
from apps.Reviews.forms import ReviewForm
from apps.Reviews.models import Review

def lista_jogos(request):
    q = request.GET.get('q')
    jogos = Jogo.objects.all()
    if q:
        jogos = jogos.filter(nome__icontains=q)
    return render(request, 'jogos/lista.html', {'jogos': jogos, 'q': q})

def detalhe_jogo(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    reviews = jogo.reviews.all().order_by('-data')
    review_form = ReviewForm()
    return render(request, 'jogos/detalhe.html', {'jogo': jogo, 'reviews': reviews, 'review_form': review_form})

@admin_required
def criar_jogo(request):
    if request.method == 'POST':
        form = JogoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jogos:lista')
    else:
        form = JogoForm()
    return render(request, 'jogos/form.html', {'form': form})

@admin_required
def editar_jogo(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    if request.method == 'POST':
        form = JogoForm(request.POST, instance=jogo)
        if form.is_valid():
            form.save()
            return redirect('jogos:detalhe', pk=jogo.pk)
    else:
        form = JogoForm(instance=jogo)
    return render(request, 'jogos/form.html', {'form': form, 'edit': True})

@admin_required
def excluir_jogo(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    if request.method == 'POST':
        jogo.delete()
        return redirect('jogos:lista')
    return render(request, 'jogos/confirm_delete.html', {'object': jogo})

@login_required_custom
def adicionar_favorito(request, pk):
    favoritos = request.session.get('favoritos', [])
    if pk not in favoritos:
        favoritos.append(pk)
        request.session['favoritos'] = favoritos
    return redirect('jogos:detalhe', pk=pk)
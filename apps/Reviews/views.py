from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from .models import Review
from pixelzone.utils import login_required_custom, get_logged_user
from apps.Jogos.models import Jogo

@login_required_custom
def criar_review(request, jogo_pk):
    jogo = get_object_or_404(Jogo, pk=jogo_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            r = form.save(commit=False)
            r.jogo = jogo
            r.usuario = get_logged_user(request)
            r.save()
    return redirect('jogos:detalhe', pk=jogo_pk)

@login_required_custom
def editar_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if review.usuario.id != request.session.get('usuario_id'):
        return redirect('jogos:detalhe', pk=review.jogo.pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('jogos:detalhe', pk=review.jogo.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/form.html', {'form': form, 'edit': True, 'review': review})

@login_required_custom
def excluir_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    usuario_id = request.session.get('usuario_id')
    is_owner = review.usuario.id == usuario_id
    user = get_logged_user(request)
    is_admin = user and getattr(user, 'is_admin', False)
    if not (is_owner or is_admin):
        return redirect('jogos:detalhe', pk=review.jogo.pk)
    if request.method == 'POST':
        jogo_pk = review.jogo.pk
        review.delete()
        return redirect('jogos:detalhe', pk=jogo_pk)
    return render(request, 'reviews/confirm_delete.html', {'object': review})
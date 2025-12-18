from django.shortcuts import render, get_object_or_404, redirect
from apps.Usuario.models import Usuario
from apps.Jogos.models import Jogo
from .models import Review
from .forms import ReviewForm
from apps.Usuario.decorators import admin_required, login_required_custom

@admin_required
def lista_reviews(request, jogo_pk):
    jogo = get_object_or_404(Jogo, pk=jogo_pk)
    reviews = Review.objects.filter(jogo=jogo).order_by('-data')

    context = {
        "jogo": jogo,
        "reviews": reviews
    }

    return render(request, "reviews/lista.html", context)

@login_required_custom
def criar_review(request, jogo_id):
    if not request.session.get('usuario_id'):
        return redirect('usuario:login')

    jogo = get_object_or_404(Jogo, pk=jogo_id)
    usuario = get_object_or_404(Usuario, pk=request.session['usuario_id'])

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.jogo = jogo
            review.usuario = usuario
            review.save()
            return redirect('jogos:detalhe', pk=jogo.id)
    else:
        form = ReviewForm()

    return render(request, 'reviews/criar.html', {
        'form': form,
        'jogo': jogo
    })

@login_required_custom
def editar_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    is_admin = request.session.get("is_admin")
    
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('usuario:login')


    if review.usuario.id != usuario_id and not is_admin:
        return redirect('jogos:detalhe', review.jogo.pk)

    if request.method == 'POST':
        review.nota = request.POST.get('nota')
        review.comentario = request.POST.get('comentario')
        review.save()
        return redirect('jogos:detalhe', review.jogo.pk)

    return render(request, 'reviews/editar.html', {'review': review})

@login_required_custom
def excluir_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    is_admin = request.session.get("is_admin")
    
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('usuario:login')

    
    if review.usuario.id != usuario_id and not is_admin:
        return redirect('jogos:detalhe', review.jogo.pk)

    if request.method == 'POST':
        jogo_pk = review.jogo.pk
        review.delete()
        return redirect('jogos:detalhe', jogo_pk)

    return render(request, 'reviews/excluir.html', {'review': review})

from django.shortcuts import render, get_object_or_404, redirect
from apps.Usuario.models import Usuario
from apps.Jogos.models import Jogo
from .models import Review

def lista_reviews(request, jogo_pk):
    jogo = get_object_or_404(Jogo, pk=jogo_pk)
    reviews = Review.objects.filter(jogo=jogo).order_by('-data')

    context = {
        "jogo": jogo,
        "reviews": reviews
    }

    return render(request, "reviews/lista.html", context)


def criar_review(request, jogo_pk):
    jogo = get_object_or_404(Jogo, pk=jogo_pk)

    if request.method == "POST":
        usuario_id = request.POST.get("usuario")
        nota = request.POST.get("nota")
        comentario = request.POST.get("comentario")

        usuario = Usuario.objects.get(pk=usuario_id)

        Review.objects.create(
            nota=nota,
            comentario=comentario,
            usuario=usuario,
            jogo=jogo
        )

        return redirect("reviews:lista", jogo_pk=jogo.pk)

    usuarios = Usuario.objects.all()

    context = {
        "usuarios": usuarios,
        "jogo": jogo
    }

    return render(request, "reviews/criar.html", context)
def editar_review(request, pk):
    review = get_object_or_404(Review, pk=pk)

    if request.method == "POST":
        review.nota = request.POST.get("nota")
        review.comentario = request.POST.get("comentario")
        review.save()
        return redirect("reviews:lista", jogo_pk=review.jogo.pk)

    return render(request, "reviews/editar.html", {
        "review": review
    })
def excluir_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        jogo_pk = review.jogo.pk  # pega o pk do jogo relacionado
        review.delete()
        return redirect('reviews:lista', jogo_pk=jogo_pk)  # passa o argumento
    return render(request, 'reviews/excluir.html', {'review': review})

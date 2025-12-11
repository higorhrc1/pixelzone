from django.shortcuts import render, redirect, get_object_or_404
from .models import Genero
from .forms import GeneroForm

def lista_generos(request):
    generos = Genero.objects.all()
    return render(request, 'genero/lista.html', {'generos': generos})

def criar_genero(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genero:lista')
    else:
        form = GeneroForm()
    return render(request, 'genero/form.html', {'form': form, 'titulo': 'Criar Gênero'})

def editar_genero(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    if request.method == 'POST':
        form = GeneroForm(request.POST, instance=genero)
        if form.is_valid():
            form.save()
            return redirect('genero:lista')
    else:
        form = GeneroForm(instance=genero)
    return render(request, 'genero/form.html', {'form': form, 'titulo': 'Editar Gênero'})

def excluir_genero(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    if request.method == 'POST':
        genero.delete()
        return redirect('genero:lista')
    return render(request, 'genero/excluir.html', {'genero': genero})

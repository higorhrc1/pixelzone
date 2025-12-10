from django.shortcuts import render, redirect, get_object_or_404
from .models import Genero
from .forms import GeneroForm
from pixelzone.utils import admin_required

def lista_generos(request):
    generos = Genero.objects.all()
    return render(request, 'genero/lista.html', {'generos': generos})

@admin_required
def criar_genero(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genero:lista')
    else:
        form = GeneroForm()
    return render(request, 'genero/form.html', {'form': form})

@admin_required
def editar_genero(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    if request.method == 'POST':
        form = GeneroForm(request.POST, instance=genero)
        if form.is_valid():
            form.save()
            return redirect('genero:lista')
    else:
        form = GeneroForm(instance=genero)
    return render(request, 'genero/form.html', {'form': form, 'edit': True})

@admin_required
def excluir_genero(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    if request.method == 'POST':
        genero.delete()
        return redirect('genero:lista')
    return render(request, 'genero/confirm_delete.html', {'object': genero})
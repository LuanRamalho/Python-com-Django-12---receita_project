from django.shortcuts import render
from .models import Receita

def lista_receitas(request):
    receitas = Receita.objects.all()
    return render(request, 'receitas/lista_receitas.html', {'receitas': receitas})

def detalhe_receita(request, pk):
    receita = Receita.objects.get(pk=pk)
    return render(request, 'receitas/detalhe_receita.html', {'receita': receita})

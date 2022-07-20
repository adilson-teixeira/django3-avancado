from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import ProdutoModelForm # retirado ContatoForm,
from .models import Produto
from django.shortcuts import redirect #usado para redirecionar usuário anonimo.
from django.views.generic import TemplateView


class IndexView(TemplateView):  #class BasedViews
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        """recupera o contexto caso contenha dados"""
        context['produtos'] = Produto.objects.all()
        #context['servicos'] = Servico.objects.all() <= quantos tiver no model/ bd
        #context['servicos'] = Servico.objects.order_by('?').all() <= exibição aleatória ? = qualquer caractere
        return context


"""def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)"""

def produto(request): #Function BasedViews
    if str(request.user) != 'AnonymousUser': # verifica se o usuário está logado
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Produto salvo com sucesso.')
                form = ProdutoModelForm() # limpa as entradas do form na página
            else:
                messages.error(request, 'Erro ao salvar o produto.')

        else:
            form = ProdutoModelForm()
        context = {
            'form': form
        }
        return render(request, 'produto.html', context )
    else:
        return redirect('index')
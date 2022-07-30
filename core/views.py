#from multiprocessing import context # verificar se não está sendo usado
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import ProdutoModelForm, CarroModelForm # retirado ContatoForm,
from .models import Produto, Post, Carro
from django.shortcuts import redirect #usado para redirecionar usuário anonimo.
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView #CRUD
from django.urls import reverse_lazy


class CarIndexView(ListView):
    models = Carro
    templante_name = 'carindex.html'
    queryset = Carro.objects.all() 
    #poderia ser usado filtros de buscas ou variável se vier da página 
    context_object_name = 'carros'



class CreateCarroView(CreateView):
    model = Carro
    template_name = 'carro_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('carindex')
    # url para quando o produto é salvo com sucesso. 


class UpdateCarroView(UpdateView):
    model = Carro
    template_name = 'carro_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('carindex')



class DeleteCarroView(DeleteView):
    model = Carro
    template_name = 'carro_del.html'
    success_url = reverse_lazy('carindex')

class IndexView(TemplateView):  #class BasedViews
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        """recupera o contexto caso contenha dados"""
        context['produtos'] = Produto.objects.all()
        context['posts'] = Post.objects.all()
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
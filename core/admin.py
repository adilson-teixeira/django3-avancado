from urllib import request
from django.contrib import admin
from .models import Produto, Post

admin.site.site_header ='Página de Administração - Django 3'
admin.site.site_title = 'Página de Administração - Django 3 -Avançado.'
admin.site.index_title = 'Avançando nos conhecimentos do Django'


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'slug', 'criado', 'modificado', 'ativo')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', '_autor') #_autor nome/método (poderia ser qualquer um) def abaixo
    """ Para que ´possa ser exibido o nome e sobre nome será criado a função _autor"""
    exclude = ['autor']

    def _autor(self, instance):
        return f'{instance.autor.get_full_name()}'

    def get_queryset(self, request):
        """Sobrescrevendo método para que usuários do Admin vejam apenas seus post."""
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(autor=request.user) #Filtrando pelo usuário logado.

    def save_model(self, request, obj, form, change):
        """Sobrescrevendo método para que o autor seja quem está logado."""
        obj.autor = request.user
        super().save_model(request, obj, form, change)
        
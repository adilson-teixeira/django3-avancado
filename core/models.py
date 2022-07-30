from django.db import models
from django.contrib.auth import get_user_model
#from stdimage.models import StdImageField

#SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Produto(Base):
    nome = models.CharField('Nome',max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    #imagem = StdImageField('imagem', upload_to='produtos', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(produto_pre_save, sender=Produto)



class Post(models.Model):
    autor = models.ForeignKey(get_user_model(), verbose_name='Autor', on_delete=models.CASCADE)
    titulo = models.CharField('Título', max_length=100)
    texto = models.TextField('Texto', max_length=400)

    def __str__(self):
        return self.titulo


class Carro(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome
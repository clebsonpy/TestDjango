from django.db import models

# Create your models here.
class Artigo(models.Model):
    class Meta:
        ordering = ('-publicacao',)

    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    publicacao = models.DateTimeField(auto_now_add=True)

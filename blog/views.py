from django.shortcuts import render
from .models import Artigo
# Create your views here.

def index(request):
    artigos = Artigo.objects.all()
    context = {'artigos':artigos}
    return render(request, 'blog/index.html', context)

def artigo(request, artigo_id):
    art = Artigo.objects.get(id=artigo_id)
    context = {'artigo':art}
    return render(request, 'blog/artigo.html', context)

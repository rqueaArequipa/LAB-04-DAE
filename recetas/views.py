from django.shortcuts import render 
from .models import Autor, Receta, Comentario
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


def Index(request):
    return render(request, 'receta/index.html')

def Recetas(request):
    autor_nombre = Autor.objects.all()
    if "registrado" in request.POST:
        contador = 0
        title = request.POST['titulo']
        for i in Receta.objects.all():
            if title == i.titulo:
                contador = contador + 1
        if contador == 0:
            nombre = request.POST['autor']
            email = nombre.lower().replace(" ","")+'@gmail.com'
            autor = Autor(nombre = nombre, email = email)
            autor.save()
            titulo = request.POST['titulo']
            ingredientes = request.POST['ingredientes']
            preparacion = request.POST['preparacion']
            imagen = request.POST['imagen']
            autor = autor
            receta = Receta(titulo = titulo, ingredientes = ingredientes,  preparacion = preparacion, imagen = imagen, autor = autor)
            receta.save()
    context = {
        'autor' : autor_nombre
    }
    return render(request, 'receta/receta.html', context)

def Preparacion(request, autor_id, receta_id):
    autor = Autor.objects.get(pk=autor_id)
    receta = autor.receta_set.get(pk=receta_id)
    if "comentado" in request.POST:
        comentario = Comentario(texto = request.POST['comentario'], receta = receta)
        comentario.save()
    context = {
        'receta' : receta,
    }
    return render(request, 'receta/preparacion.html', context)

def Register(request):
    return render(request, 'receta/register.html')

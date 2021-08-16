from django.shortcuts import render, redirect
from .models import *


##al abrir la pagina,lo primero que se ve es esto,el index.
def index(request):
    if request.method == 'GET':
        context = {
        'books': Book.objects.all(),
    }
    return render(request, 'index.html', context)

#lo que esta en parentesis,es el nombre que proviene del post,revisar el index 
def procesarlibro(request):
    print (request.POST)
    books = Book.objects.create(
        title=request.POST.get('Titulo_libro'),
        desc=request.POST.get('Descripcion_libro'),
    )
    return redirect("/books")


def ingresar_un_libro(request):
    print (request.POST)
    books = Book.objects.create(
        title=request.POST.get('Titulo_libro'),
        desc=request.POST.get('Descripcion_libro'),
    )
    return redirect("books/{{book.id}}")

def procesarautor(request):
    print (request.POST)
    author= Author.objects.get(
        id=request.POST.get('author'),
)
    author= Author.objects.create(
        first_name=request.POST.get('first_name_Author'),
        last_name=request.POST.get('last_name_Author'),
        notas=request.POST.get('notas_Author'),
    )

    return redirect("/procesarautor")

def eliminarautor(request,author):
    print(author)
    
    author= Author.objects.get(id=author),
    author.delete()
    return redirect("/")







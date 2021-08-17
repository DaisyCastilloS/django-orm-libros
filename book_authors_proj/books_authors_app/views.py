from django.shortcuts import render, redirect
from .models import *


##al abrir la pagina,lo primero que se ve es esto,el index.
def index(request):
    if request.method == 'GET':
        context = {
        'books': Book.objects.all(),
    }
    return render(request, 'index.html', context)

#lo que esta en parentesis,es el nombre que proviene del post,revisar el index.
#aqui estoy añadiendo un libro a una lista a traves de formulario  y se redirige al index
def procesarlibro(request):
    
    print (request.POST)
    books = Book.objects.create(
        title=request.POST.get('Titulo_libro'),
        desc=request.POST.get('Descripcion_libro'),
        
    )
    return redirect('/')

##-----------------------------------------------------------------

## una vez que se crea la lista,necesito acceder a la info de cada 
# libro (que esta en el template index.html),con un get, y mostrarla en el  libro.html
def libro(request,id):
    book= Book.objects.get(id=id)
    context = {
        'book' : book
    }
    return render(request,'libro.html',context)



# una vez que tengo un libro seleccionado,creo la informacion de ese libro y la redirijo a ("book/{{book.id}}")
def ingresar_un_libro(request):
    print (request.POST)
    books = Book.objects.create(
        title=request.POST.get('Titulo_libro'),
        desc=request.POST.get('Descripcion_libro'),
    )
    return redirect("book/{{book.id}}")


###----------------------------------------------
## una vez que tengo ese libro,necesito asociarlo con un autor de los que ya estan

def autor(request,id):
    author = Author.objects.get(id=id)
    context = {
        'author' : author
    }
    return render(request,'autor.html',context)

#en caso de que ese libro no se asocie a ninguno de los autores ya creados antes,se crea un autor
def ingresar_un_autor(request):
    author= Author.objects.create(
        first_name=request.POST.get('first_name_Author'),
        last_name=request.POST.get('last_name_Author'),
        notas=request.POST.get('notas_Author'),
    )

    return redirect("author/{{author.id}}")

###---------------------------------------------------------

#una vez que se crea un autor, necesito obtener todos los autores
def authors(request):
    if request.method == 'GET':
        context = {
        'authors': Author.objects.all(),
    }
    return render(request, 'add_autor.html', context)


#una vez que tengo a todos los autores,
def procesarautor(request):
    
    print (request.POST)
    author= Author.objects.create(
        first_name=request.POST.get('first_name_Author'),
        last_name=request.POST.get('last_name_Author'),
        notas=request.POST.get('notas_Author'),
    )

    return redirect("author/{{author.id}}")






def eliminarautor(request,author):
    print(author)
    
    author= Author.objects.get(id=author),
    author.delete()
    return redirect("/")







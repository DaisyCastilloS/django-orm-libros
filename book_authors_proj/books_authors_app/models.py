from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=45,verbose_name='Titulo')
    desc = models.TextField(verbose_name= "Descripcion")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    action = models.CharField(max_length=45,default="Ver")
    ##Authors = models.ManyToManyField("Author",related_name="books") esta es la relacion inversa
    def __repr__(self):
        return f"{self.title} {self.desc}"
    def __str__(self):
        return f"{self.title} {self.desc}"

class Author(models.Model):
    first_name = models.CharField(max_length=255,verbose_name="First Name")
    last_name = models.CharField(max_length=255,verbose_name="Last Name")
    books = models.ManyToManyField(Book, related_name="Authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notas = models.TextField ()
    
    def __repr__(self):
        return f"<Author object: {self.first_name} ({self.last_name})>"
    
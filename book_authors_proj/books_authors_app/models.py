from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=45)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    action = models.CharField(max_length=45,default="Ver")
    
    def __repr__(self):
        return f"<Book object: {self.title} {self.desc} >"
    

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="libro")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notas = models.TextField ()
    
    def __repr__(self):
        return f"<Author object: {self.first_name} ({self.last_name})>"
    
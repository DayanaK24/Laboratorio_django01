from django.db import models

# Create your models here.
class Libro(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    #rama pruebaLibros. agregando nuevo tipo de dato
    cover_image = models.ImageField(upload_to='covers/', null=True, blank=True)

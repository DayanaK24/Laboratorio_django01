from django.db import models

# Create your models here.
class Usuario(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Para usar un hash seguro
    created_at = models.DateTimeField(auto_now_add=True)
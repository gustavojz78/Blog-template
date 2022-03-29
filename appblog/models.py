from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=400)
    def __str__(self):
        return (f"User: {self.user}, password: {self.password}")

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=30)
    def __str__(self):
        return (f"category: {self.category}")

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=4000)
    createdAt = models.DateTimeField(auto_now_add=True) #Agrega automáticamente la fecha a la hora de crearse
    author = models.CharField(max_length=100)
    def __str__(self):
        return (f"id: {self.id}, author: {self.author}, createdAt: {self.createdAt}")
    



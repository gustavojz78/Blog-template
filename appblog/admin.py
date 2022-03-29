from django.contrib import admin
from .models import Usuario, Category, Post

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Category)
admin.site.register(Post)
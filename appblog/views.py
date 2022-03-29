from django.shortcuts import render

from .forms import PostForm, UserSearchForm
from .models import Post, Usuario, Category

# Create your views here.
def inicio(request):
    categories = Category.objects.all()
    return render(request, 'appblog/index.html', {"categories": categories})

def my_profile(request):
    categories = Category.objects.all()
    return render(request, 'appblog/myprofile.html', {"categories": categories})

def posts_view(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'appblog/posts.html', {"posts": posts, "categories": categories})

def create_post(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    formulario = PostForm()
    #Cuando se envían los datos entra a POST
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            curso = Post(content=data['content'],author=data['author'])
            curso.save()
            return render(request, 'appblog/createPost.html', {'formulario': formulario, "categories": categories})
    #Cuando hay un get
    else :
        return render(request, 'appblog/createPost.html', {'formulario': formulario, "categories": categories})

def search_user(request):
    form_search_user = UserSearchForm()
    data = request.GET.get('user', "")
    if data:
        print(data)
        form_with_data = UserSearchForm(request.GET)
        if form_with_data.is_valid():
            perfil = Usuario.objects.filter(user=data).first()
            print (perfil)
            if (perfil):
                return render(request, 'appblog/busqueda_usuario.html', {"search_form": form_search_user,"usuario": perfil})
            return render(request, 'appblog/busqueda_usuario.html', {"search_form": form_search_user,"usuario": None})

        return render(request, 'appblog/busqueda_usuario.html', {"search_form": form_search_user, "usuario": perfil, "error": form_with_data.errors})
    
    return render(request, 'appblog/busqueda_usuario.html', {"search_form": form_search_user, "usuario": None, "error": None})

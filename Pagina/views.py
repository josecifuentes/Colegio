from django.shortcuts import render
from .models import Post
from administracion.models import Actividade
from .forms import PostForm
from django.shortcuts import redirect
# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def acti(request, pk):
    actividad = Actividade.objects.filter(Grupo__iexact='Todos').order_by('-Fecha_Inicio')
    pag=pk;
    inicio=(pk-1)*5;
    fin=pk*5;
    num=int((actividad.count()/5)-0.2)+1;
    list = []
    for i in range(1,num+1):
        list.append(i)
    return render(request, 'Pagina/actividades.html', {'actividad': actividad,'inicio': inicio,'fin': fin,'list': list,'pag': pag})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'Pagina/inicio.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'Pagina/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'Pagina/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'Pagina/post_edit.html', {'form': form})
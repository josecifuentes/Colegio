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

def home(request):
    return render(request, 'Pagina/inicio.html')

def grade(request):
    return render(request, 'Pagina/inicio.html')

def news(request):
    return render(request, 'Pagina/inicio.html')

def downloads(request):
    return render(request, 'Pagina/downloads.html')

def download_content(request, pk):
    content = ""
    correos = ""
    calendario = ""
    if(pk==1):
        content="cursos/1a.pdf"
        calendario = "horarios/B1A.pdf"
    if(pk==2):
        content="cursos/1b.pdf"
        calendario = "horarios/B1B.pdf"
    if(pk==3):
        content="cursos/2a.pdf"
        calendario = "horarios/B2A.pdf"
    if(pk==4):
        content="cursos/2b.pdf"
        calendario = "horarios/B2B.pdf"
    if(pk==5):
        content="cursos/3a.pdf"
        calendario = "horarios/B3A.pdf"
    if(pk==6):
        content="cursos/3b.pdf"
        calendario = "horarios/B3B.pdf"
    if(pk==7):
        content="cursos/4tosalud.pdf"
        calendario = "horarios/4toEsalud.pdf"
    if(pk==8):
        correos = "cursos/4todiseno_correos.pdf"
        content="cursos/4todiseno.pdf"
        calendario = "horarios/4toEdiseno.pdf"
    if(pk==9):
        correos = "cursos/4tojuridicas_correos.pdf"
        content="cursos/4tojuridicas.pdf"
        calendario = "horarios/4toEJuridicas.pdf"
    if(pk==10):
        content="cursos/4tocompu.pdf"
        calendario = "horarios/4toEComputacion.pdf"
    if(pk==11):
        content="cursos/5tocompu.pdf"
    if(pk==12):
        content="cursos/5toelectronica.pdf"
    if(pk==13):
        content="cursos/5tosalud.pdf"
    if(pk==14):
        correos = "cursos/5todiseno_correos.pdf"
        content="cursos/5todiseno.pdf"
    if(pk==15):
        content="cursos/guiamaes.pdf"
    if(pk==16):
        content=""
    return render(request, 'Pagina/download_content.html',{'content':content,'correos':correos,'calendario':calendario})

def about(request):
    return render(request, 'Pagina/inicio.html')

def contact(request):
    return render(request, 'Pagina/inicio.html')

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
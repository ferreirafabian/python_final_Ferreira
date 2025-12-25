from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from django.db.models import Sum

def inicio(request):
    posts = Post.objects.all().order_by('-fecha')
    return render(request, 'blog/inicio.html', {'posts': posts})

@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('inicio')
    else:
        form = PostForm()
    return render(request, 'blog/crear_post.html', {'form': form})

@login_required
def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.user == request.user:
        post.delete()
    return redirect('inicio')

@login_required
def estadisticas(request):
    posts = Post.objects.filter(user=request.user)
    total_kms = posts.aggregate(Sum('kilometros'))['kilometros__sum'] or 0
    total_dinero = posts.aggregate(Sum('dinero'))['dinero__sum'] or 0
    total_pedidos = posts.aggregate(Sum('pedidos'))['pedidos__sum'] or 0
    return render(request, 'blog/estadisticas.html', {
        'total_kms': total_kms,
        'total_dinero': total_dinero,
        'total_pedidos': total_pedidos
    })

def buscar_fecha(request):
    fecha = request.GET.get('fecha')
    posts = Post.objects.filter(fecha=fecha) if fecha else []
    return render(request, 'blog/buscar_fecha.html', {'posts': posts})

def acerca_de_mi(request):
    return render(request, 'blog/acerca_de_mi.html')

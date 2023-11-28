from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from phones.forms import *
from phones.models import *

menu=['Apple', 'Android', 'Samsung', 'iPhone']

def index(request):
    posts = Phones.objects.all()
    context = {
        'posts': posts,
        'title': 'Application phones',
        'menu': menu,
        'cat_selected': '',
        'unwrap': False
    }
    return render(request, 'phones/index.html', context=context)

def about(request):
    return render(request, 'phones/about.html', {'title': 'О сайте', 'menu': menu})

def android(request):
    return HttpResponse("Android")

def iphone(request):
    return HttpResponse("iPhone")

def samsung(request):
    return HttpResponse("Samsung")


def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def show_category(request, cat_slug):
    posts = Phones.objects.all()
    context = {
        'posts': posts,
        'title': 'Application phones',
        'menu': menu,
        'cat_selected': cat_slug,
        'unwrap': False
    }
    return render(request, 'phones/index.html', context=context)

def dg(request):
    return HttpResponse('<h1>dg</h1>')

def nokia(request):
    return HttpResponse('Nokia')

def blackview(request):
    return HttpResponse("BlackView")

def show_post(request, post_id):
    post = get_object_or_404(Phones, pk=post_id)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
        'unwrap': False
    }
    return render(request, 'phones/post.html', context=context)

def secr(request):
    s=security.objects.all()
    context={
        's': s,
    }
    return render(request, 'phones/secr.html', context=context)

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form=AddPostForm()
    context={
        'form': form,
        'menu': menu,
        'title': 'Добавление статьи'
    }
    return render(request, 'phones/addpage.html', context=context)
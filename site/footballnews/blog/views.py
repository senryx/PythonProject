from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

from blog.forms import AddPostForm
from blog.models import *

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FIlES)
        if form.is_valid():
            #print(form.cleaned_data)
            form.save()
            return redirect('Home')
    else:
        form = AddPostForm()
    return render(request, 'blog/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def show_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'blog/post.html', context=context)


def show_category(request, cat_id):
    posts = Post.object.filter(cat_id=cat_id)
    #cats = Category.object.all()

    if len(posts) == 0:
        raise HttpResponseNotFound

    context = {
        'post': posts,
        #'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': cat_id,
    }

    return render(request, 'blog/index.html', context=context)


def index(request, cat_id):
    posts = Post.object.all()

    context = {
        'post': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, 'blog/index.html', context=context)


def about(request):
    return render(request, 'blog/about.html', {'menu': menu, 'title': 'О нас'})


def categories(request, cat):
    return HttpResponse(f"<h1>Статьи по категориям<h1><p>{cat}</p>")


def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам<h1><p>{year}</p>")


def page_not_found(request, exceprion):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
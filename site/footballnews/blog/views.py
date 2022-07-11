from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def index(request):
    return render(request, 'blog/index.html', {'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'blog/about.html', {'menu': menu, 'title': 'О нас'})


def categories(request, cat):
    return HttpResponse(f"<h1>Статьи по категориям<h1><p>{cat}</p>")


def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам<h1><p>{year}</p>")


def page_not_found(request,exceprion):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
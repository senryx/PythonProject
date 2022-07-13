from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from blog.forms import AddPostForm, RegisterUserForm
from blog.models import *
from blog.utils import DataMixin


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        #{'title': "Войти", 'url_name': 'login'}
]


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))



def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            #print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'blog/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def show_post(request, post_slug):
    post = get_object_or_404(Post, pk=post_slug)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'blog/post.html', context=context)


def show_category(request, cat_id):
    posts = Post.objects.filter(cat_id=cat_id)
    #cats = Category.objects.all()

    if len(posts) == 0:
        raise HttpResponseNotFound

    context = {
        'post': posts,
        #'cats': cats,
        'menu': menu,
        'title': 'Оттображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'blog/index.html', context=context)


def index(request):
    posts = Post.objects.all()

    context = {
        'post': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
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
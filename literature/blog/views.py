from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from .forms import CommentForm
from .models import *
from django.db.models import F
from django.contrib import messages

"""
Genre / Series / Author / Post / Comment
@login_required декоратор для доступа авторизованных юзеров
LoginRequiredMexin для доступа авторизованных юзеров

"""


class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'  # имя к которому обращатся в html
    paginate_by = 3

    def get_queryset(self):
        """
        фильтр

        """
        # return Post.objects.filter(is_published=True)
        return Post.published.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        context['subtitle'] = 'Вся литература'
        return context


class PostGenre(ListView):
    """
    жанры
    """
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 3
    allow_empty = False  # ошибка при пустой категории

    def get_queryset(self):
        print(self.kwargs)

        return Post.published.filter(genre__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Genre.objects.get(slug=self.kwargs['slug'])
        context['subtitle'] = 'Жанры'
        return context


class PostAuthor(ListView):
    """
    Автор
    """
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 3
    allow_empty = False  # ошибка при пустой категории

    def get_queryset(self):
        print(self.kwargs)

        return Post.published.filter(author__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Author.objects.get(slug=self.kwargs['slug'])
        context['subtitle'] = 'Автор'
        return context


class PostSeries(ListView):
    """
    серии книг
    """
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 3
    allow_empty = False  # ошибка при пустой категории

    def get_queryset(self):
        return Post.published.filter(series__slug=self.kwargs['slug']).order_by('number_series')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Series.objects.get(slug=self.kwargs['slug'])
        context['subtitle'] = 'Серия книг'
        return context


class GetPost(DetailView):
    """
    Вывод Поста
    пост выводится с помощью get_absolute_url
    """
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'
    allow_empty = False  # ошибка если пустой пост

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        для количества просмотров
        """
        context = super().get_context_data(**kwargs)

        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        context['form'] = CommentForm
        return context


class CommentBook(SuccessMessageMixin, CreateView):
    """
    Подключаем комментарии к посту
    """
    form_class = CommentForm  # форма
    success_message = "Комментарий отправлен"


    def form_valid(self, form):
        """
        связываем коммент к посту, формируем запись без занесения в бд,
        определяем пользователя , после сохраняем в бд
        """
        form.instance.com_id = self.kwargs.get("pk")
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        return super().form_valid(form)


    def get_success_url(self):
        """действе после отправки комента , остается на странице"""

        return self.object.com.get_absolute_url()


class Search(ListView):
    """
    Поиск
    """
    template_name = "blog/search.html"
    context_object_name = "posts"
    paginate_by = 3

    def get_queryset(self):
        return Post.published.filter(title__icontains=self.request.GET.get("s"))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Поиск'
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context


@login_required
def about(request):
    """
    LOGIN_URL = 'user:login'  в сеттингах - редирект
    """

    return render(request, 'blog/about.html', {messages: 'messages'})


def page_not_found(request, exception):
    """

    обработчик 404
    в настройках выключить дебаг
    нужно прописать handler404 = page_not_found в общих урлах
    """
    # return HttpResponseNotFound("<h1>Страница не найдена</h1>")
    return redirect('/')

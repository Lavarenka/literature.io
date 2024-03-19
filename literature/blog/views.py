from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import *
from django.db.models import F

"""
Genre / Series / Author / Post / Comment
"""


class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
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
        return Post.published.filter(genre__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Genre.objects.get(slug=self.kwargs['slug'])
        context['subtitle'] = 'Жанры'
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
    """
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        для количества просмотров
        """
        context = super().get_context_data(**kwargs)

        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


def page_not_found(request, exception):
    """

    обработчик 404
    в настройках выключить дебаг
    нужно прописать handler404 = page_not_found в общих урлах
    """
    # return HttpResponseNotFound("<h1>Страница не найдена</h1>")
    return redirect('/')

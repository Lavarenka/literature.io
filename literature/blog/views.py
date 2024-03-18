from django.shortcuts import render
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
        return context


class PostGenre(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 3
    allow_empty = False # ошибка при пустой категории

    def get_queryset(self):
        return Post.published.filter(genre__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Genre.objects.get(slug=self.kwargs['slug'])
        return context


def PostSeries(request):
    series = Post.published.filter(series__slug=Post.pk)


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
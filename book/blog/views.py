from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import F
from blog.models import Post, Genre


class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'  # имя к которому обращатся в html
    paginate_by = 20

    def get_queryset(self):
        """
        фильтр

        """
        return Post.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        context['subtitle'] = 'Вся литература'
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
        return context


class PostGenre(ListView):
    """
    жанры
    """
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 20
    allow_empty = False  # ошибка при пустой категории

    def get_queryset(self):
        return Post.objects.filter(genre__slug=self.kwargs['slug']).filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Genre.objects.get(slug=self.kwargs['slug'])
        context['subtitle'] = 'Жанры'
        return context

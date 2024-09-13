from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, CreateView
from django.db.models import F
from django.core.paginator import Paginator

from blog.forms import CommentForm
from blog.models import Post, Genre, Series, Comment, Author


class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'  # имя к которому обращатся в html
    paginate_by = 24

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

        context['form'] = CommentForm
        post = self.get_object()
        try:
            context['series_book'] = post.series.post.filter(is_published=True).select_related().order_by('number_series')
        except:
            context['series_book'] = None



        return context


class PostGenre(ListView):
    """
    жанры
    """
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 24
    allow_empty = False  # ошибка при пустой категории

    def get_queryset(self):
        return Post.objects.filter(genre__slug=self.kwargs['slug']).filter(is_published=True)

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
    paginate_by = 24
    allow_empty = False  # ошибка при пустой категории

    def get_queryset(self):
        return Post.objects.filter(author__slug=self.kwargs['slug']).filter(is_published=True)

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

    allow_empty = False  # ошибка при пустой категории

    def get_queryset(self):
        return Post.objects.filter(series__slug=self.kwargs['slug']).filter(is_published=True).order_by('number_series')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Series.objects.get(slug=self.kwargs['slug'])
        context['subtitle'] = 'Серия книг'

        return context



class PostFilter(View):

    def get(self, request, *args, **kwargs):
        value = request.GET.get('sort')
        page_number = request.GET.get('page', 1)  # Получаем номер страницы из GET-параметров

        if value:
            content = Post.objects.filter(is_published=True).order_by(value).reverse()
        else:
            content = Post.objects.filter(is_published=True)

        # Создаем объект Paginator с количеством постов на странице
        paginator = Paginator(content, 24)  # 10 постов на страницу

        # Получаем нужную страницу
        page_obj = paginator.get_page(page_number)

        return render(request, 'blog/index.html', {'posts': page_obj})




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





class DelComment(View):
    def get(self, request, **kwargs):
        pk = kwargs['pk']
        comment = Comment.objects.get(id=pk)
        if comment:
            comment.delete()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])




class Search(ListView):
    """
    Search for icontains is case insensitive.
    """
    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 24

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get("s")).filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Поиск'
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, CreateView
from django.db.models import F
from django.core.paginator import Paginator
from blog.forms import CommentForm
from blog.models import Post, Genre, Series, Comment, Author


class Home(ListView):
    """ render of all published posts """
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'  # name for the link in the template
    paginate_by = 24

    def get_queryset(self):
        """ filter, render only published """
        return Post.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        context['subtitle'] = 'Вся литература'
        return context


class GetPost(DetailView):
    """
    post detail
    the post is output using get_absolute_url
    """
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'
    allow_empty = False  # error if empty post

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        for the number of views
        """
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1  # expression: db level position
        self.object.save()  # save db
        self.object.refresh_from_db()  # requesting new data

        context['title'] = Post.objects.get(pk=self.object.pk).title
        context['form'] = CommentForm
        post = self.get_object()  # to display all books in the series
        try:
            context['series_book'] = post.series.post.filter(is_published=True).order_by(
                'number_series')
        except:
            # if there are no series in the book, then it does not display an error
            context['series_book'] = None

        return context


class PostGenre(ListView):
    """
    sort books by genre
    """
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 24
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(genre__slug=self.kwargs['slug']).filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Genre.objects.get(slug=self.kwargs['slug'])
        context['subtitle'] = 'Жанры'
        return context


class PostAuthor(ListView):
    """
    sort books by author
    """
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 24
    allow_empty = False  # error if empty post

    def get_queryset(self):
        return Post.objects.filter(author__slug=self.kwargs['slug']).filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Author.objects.get(slug=self.kwargs['slug'])
        context['subtitle'] = 'Автор'
        return context


class PostSeries(ListView):
    """
    sort books by series
    """
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    allow_empty = False  # error if empty post

    def get_queryset(self):
        return Post.objects.filter(series__slug=self.kwargs['slug']).filter(is_published=True).order_by('number_series')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Series.objects.get(slug=self.kwargs['slug'])
        context['subtitle'] = 'Серия книг'

        return context


class PostFilter(View):
    """
    filter the posts
    as a get query takes the value: views, time_create, - time_create, year and sorts by value
    """

    def get(self, request, *args, **kwargs):
        value = request.GET.get('sort')
        page_number = request.GET.get('page', 1)  # Getting page number from GET parameters

        if value:
            content = Post.objects.filter(is_published=True).order_by(value).reverse()
        else:
            content = Post.objects.filter(is_published=True)

        # Create a Paginator object with the number of posts per page
        paginator = Paginator(content, 24)  # 24 posts per page

        # We get the required page
        page_obj = paginator.get_page(page_number)

        return render(request, 'blog/index.html', {'posts': page_obj, 'title': 'Фильтр'})


class CommentBook(SuccessMessageMixin, CreateView):
    """
    Connecting comments to a post
    """
    form_class = CommentForm  # form
    success_message = "Комментарий отправлен"

    def form_valid(self, form):
        """
        we link the comment to the post,
        form a record without entering it into the database
        we define the user, then save it into the database
        """
        form.instance.com_id = self.kwargs.get("pk")
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        """ actions after sending a comment, remains on the page """
        return self.object.com.get_absolute_url()


class DelComment(View):
    """
    delete comment
    """

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
    template_name = "blog/search.html"
    context_object_name = "posts"
    paginate_by = 24

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get("s")).filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Поиск'
        context['s'] = f"s={self.request.GET.get('s')}&"  # for paginate
        return context

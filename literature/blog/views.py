from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

"""
Genre / Series / Author / Post / Comment
"""


class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.published.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context


def index(request):
    return render(request, 'blog/index.html')

def get_genre(request, slug):
    return render(request, 'blog/genre.html')

def get_post(request, slug):
    return render(request, 'blog/genre.html')
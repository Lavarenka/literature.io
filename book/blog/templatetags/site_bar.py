from django import template
from django.db.models import Count

from blog.models import Genre, Author, Series

register = template.Library()

@register.inclusion_tag('blog/genre_tpl.html')
def show_genre(genre_class='genre'):
    genres = Genre.objects.filter(genre__is_published=True).annotate(total=Count('genre'))
    return {"genres": genres, "genre_class": genre_class}

@register.inclusion_tag('blog/author_tpl.html')
def show_author(author_class='author'):
    authors = Author.objects.filter(author__is_published=True).annotate(total=Count('author'))
    return {"authors": authors, "author_class": author_class}

@register.inclusion_tag('blog/series_tpl.html')
def show_series(series_class='series'):
    series = Series.objects.filter(post__is_published=True).annotate(total=Count('post'))
    return {"series": series, "series_class": series_class}
from django import template
from django.db.models import Count

from blog.models import Genre

register = template.Library()

@register.inclusion_tag('blog/genre_tpl.html')
def show_genre(genre_class='genre'):
    genres = Genre.objects.annotate(total=Count('genre')).filter(genre__is_published=True)
    return {"genres": genres, "genre_class": genre_class}
from django import template
from django.db.models import Count

from blog.models import Genre

register = template.Library()

@register.inclusion_tag('blog/genre_tpl.html')
def show_genre(genre_class='genre'):
    genres = Genre.objects.annotate(total=Count('genre')).filter(total__gt=0)
    return {"genres": genres, "genre_class": genre_class}
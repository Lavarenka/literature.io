from django import template
from blog.models import Genre

register = template.Library()

@register.inclusion_tag('blog/genre_tpl.html')
def show_genre(genre_class='genre'):
    genres = Genre.objects.all()
    return {"genres": genres, "genre_class": genre_class}
from django import template
from django.db.models import Count

from blog.models import Post

register = template.Library()


@register.inclusion_tag('blog/popular_post.html')
def get_popular(cnt=16):
    """cnt количество постов. В штмл можно изменить"""
    posts = Post.objects.filter(is_published=True).order_by('-time_create')[:cnt]
    return {"posts": posts, }
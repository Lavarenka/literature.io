from django import template
from django.db.models import Count

from blog.models import Post

register = template.Library()


@register.inclusion_tag('blog/popular_post.html')
def get_popular(cnt=3):
    """cnt3 количество постов. В штмл можно изменить"""
    posts = Post.published.order_by('-views')[:cnt]
    return {"posts": posts, }

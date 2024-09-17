from django import template
from blog.models import Post

register = template.Library()


@register.inclusion_tag('blog/popular_post.html')
def get_popular(cnt=16):
    """ cnt number of posts. In the template you can change """
    posts = Post.objects.filter(is_published=True).order_by('-time_create')[:cnt]
    return {"posts": posts, }

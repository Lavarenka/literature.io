from django import template
from about.models import SocialItem


register = template.Library()


@register.inclusion_tag("about/social_icons.html")
def get_social_icons():
    """all icons for footer"""
    icons = SocialItem.objects.all()
    return {"icons": icons}
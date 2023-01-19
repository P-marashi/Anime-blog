from django import template
from ..models import Category

register = template.Library()


@register.simple_tag
def title():
    return "Anime-weblog"



@register.inclusion_tag("blogs/inclusion_tag/slug_tag.html")


def slug_nbar():
    return {
        "category": Category.objects.filter(status="True")
    }

@register.inclusion_tag("blogs/inclusion_tag/slug_tag.html")

def pub_img():
    return {
        "category": Category.objects
    }

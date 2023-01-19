from django import template

register = template.Library()


@register.simple_tag
def title():
    return "Anime-weblog"




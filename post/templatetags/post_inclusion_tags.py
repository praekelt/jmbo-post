from django import template

register = template.Library()


@register.inclusion_tag('post/inclusion_tags/post_detail.html')
def post_detail(obj):
    return {'object': obj}

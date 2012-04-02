from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from post.models import Post
from jmbo.generic.views import GenericObjectDetail, GenericObjectList
from jmbo.view_modifiers import DefaultViewModifier


class ObjectList(GenericObjectList):
    def get_extra_context(self, *args, **kwargs):
        return {'title': _('Posts')}

    def get_view_modifier(self, request, *args, **kwargs):
        return DefaultViewModifier(request, *args, **kwargs)

    def get_paginate_by(self, *args, **kwargs):
        return 12

    def get_queryset(self, *args, **kwargs):
        return Post.permitted.all()

object_list = ObjectList()


class ObjectDetail(GenericObjectDetail):
    def get_queryset(self, *args, **kwargs):
        return Post.permitted.all()

    def get_extra_context(self, *args, **kwargs):
        return {'title': 'Posts'}

    def get_view_modifier(self, request, *args, **kwargs):
        return DefaultViewModifier(
            request,
            base_url=reverse("object_list", args=['post', 'post']),
            ignore_defaults=True,
            *args,
            **kwargs
        )

object_detail = ObjectDetail()

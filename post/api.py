from django.conf.urls import url

from tastypie.resources import ModelResource
from jmbo.api import ModelBaseResource

from post.models import Post


class PostResource(ModelBaseResource):

    class Meta:
        queryset = Post.permitted.all()
        resource_name = 'post'

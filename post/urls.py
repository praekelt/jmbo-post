from django.conf.urls.defaults import patterns, url

from jmbo.urls import v1_api

from post.api import PostResource


v1_api.register(PostResource())

urlpatterns = patterns(
    'post.views',
    url(r'^(?P<slug>[\w-]+)/$', 'object_detail', name='post_object_detail'),
)

from django.conf.urls.defaults import patterns, url

from jmbo.urls import v1_api

from post.api import PostResource


v1_api.register(PostResource())

# xxx: may need to include ckeditor urls here. check!

urlpatterns = patterns(
    '',
    url(r'^(?P<slug>[\w-]+)/$', 'jmbo.views.object_detail', name='post_object_detail'),
)

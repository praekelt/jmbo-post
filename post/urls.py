from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'post.views',
    url(r'^(?P<slug>[\w-]+)/$', 'object_detail', name='post_object_detail'),
)

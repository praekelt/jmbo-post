from django.conf.urls import patterns, include, url

from jmbo.urls import v1_api
from jmbo.views import ObjectDetail

from post.api import PostResource


v1_api.register(PostResource())

# xxx: may need to include ckeditor urls here. check!

urlpatterns = patterns(
    '',
    url(
        r'^(?P<category_slug>[\w-]+)/(?P<slug>[\w-]+)/$',
        ObjectDetail.as_view(),
        name='post_categorized_object_detail'
    ),
    url(
        r'^(?P<slug>[\w-]+)/$',
        ObjectDetail.as_view(),
        name='post_object_detail'
    ),
)

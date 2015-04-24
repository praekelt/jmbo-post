from django.conf.urls import url

from tastypie.resources import ModelResource
from jmbo.api import ModelBaseResource

from post.models import Post


class PostResource(ModelBaseResource):

    class Meta:
        queryset = Post.permitted.all()
        resource_name = 'post'

    def override_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/(?P<slug>[\w-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
        ]
